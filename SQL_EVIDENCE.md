# SQL Evidence

This page collects SQL examples from my portfolio projects and explains what each query demonstrates. The goal is to make the analytical work easy to review without requiring a full local setup.

## Source Query Files

- Subscription analytics queries: https://github.com/Abionit/subscription-analytics-lab/blob/main/sql/portfolio_queries.sql
- SOC analytics queries: https://github.com/Abionit/soc-home-lab/blob/portfolio/soc-home-lab-v2/sql/portfolio_queries.sql

## Coverage Summary

| Area | Query evidence | Demonstrates |
| --- | --- | --- |
| KPI reporting | Latest monthly KPI snapshot | sorting, limiting, metric selection, business reporting |
| Retention analysis | Cohort retention by signup month and tenure | cohort logic, ordered outputs, retention metrics |
| Churn risk | Current high-risk accounts with revenue exposure | subqueries, filtering, prioritization, risk segmentation |
| Segment analysis | Monthly plan mix and regional health | grouped business reporting and trend review |
| SOC reporting | Executive alert KPI snapshot | conditional aggregation and operational metrics |
| Alert trends | Alert volume by hour | date functions, grouping, trend reporting |
| Rule performance | Rule-level workload and SLA flags | grouped metrics, average timing, SLA analysis |
| Backlog review | Active alerts by severity and status | operational filtering and prioritization |

## Subscription Analytics Examples

### Latest Monthly KPI Snapshot

Business question: what does the latest revenue and retention trend look like?

```sql
SELECT
    metric_month,
    active_customers,
    mrr,
    arpa,
    logo_churn_rate_pct,
    net_revenue_retention_pct
FROM monthly_kpis
ORDER BY metric_month DESC
LIMIT 6;
```

This query demonstrates metric selection, ordered time-series review, and concise KPI reporting.

### Cohort Retention

Business question: how does retention behave across customer signup cohorts?

```sql
SELECT
    signup_month,
    months_since_signup,
    retained_customers,
    cohort_size,
    retention_rate_pct
FROM cohort_retention
ORDER BY signup_month, months_since_signup;
```

This query demonstrates cohort-based analysis and structured ordering for retention review.

### High-Risk Accounts With Revenue Exposure

Business question: which customers should be prioritized because their risk score and revenue exposure are high?

```sql
SELECT
    customer_id,
    company_name,
    region,
    plan_name,
    ending_mrr,
    risk_score,
    risk_band,
    payment_failures,
    high_priority_tickets,
    avg_csat
FROM customer_monthly_metrics
WHERE metric_month = (SELECT MAX(metric_month) FROM customer_monthly_metrics)
  AND risk_band = 'high'
ORDER BY risk_score DESC, ending_mrr DESC;
```

This query demonstrates subqueries, filtering, risk segmentation, and prioritization by business impact.

### Regional Health Summary

Business question: which regions show the strongest or weakest customer health signals?

```sql
SELECT
    metric_month,
    region,
    mrr,
    avg_csat,
    avg_risk_score,
    high_risk_accounts
FROM regional_health_summary
ORDER BY metric_month DESC, mrr DESC;
```

This query demonstrates segment-level reporting across revenue, satisfaction, and risk metrics.

## SOC Analytics Examples

### Executive Alert KPI Snapshot

Operational question: what is the current alert workload and SLA position?

```sql
SELECT
    COUNT(*) AS total_alerts,
    SUM(CASE WHEN severity = 'critical' THEN 1 ELSE 0 END) AS critical_alerts,
    SUM(CASE WHEN status IN ('open', 'investigating') THEN 1 ELSE 0 END) AS active_alerts,
    ROUND(AVG(triage_minutes), 1) AS avg_triage_minutes,
    ROUND(AVG(resolution_minutes), 1) AS avg_resolution_minutes,
    SUM(CASE WHEN sla_breached = 1 THEN 1 ELSE 0 END) AS sla_breaches
FROM alerts;
```

This query demonstrates conditional aggregation, averages, rounding, and operational KPI design.

### Alert Trend By Hour

Operational question: when are alerts being detected and how many are critical?

```sql
SELECT
    strftime('%Y-%m-%d %H:00:00', detected_at) AS alert_hour,
    COUNT(*) AS alert_count,
    SUM(CASE WHEN severity = 'critical' THEN 1 ELSE 0 END) AS critical_alerts
FROM alerts
GROUP BY strftime('%Y-%m-%d %H:00:00', detected_at)
ORDER BY alert_hour;
```

This query demonstrates time bucketing, grouping, ordering, and trend reporting.

### Rule-Level Performance And Workload

Operational question: which detection rules generate the most workload and SLA pressure?

```sql
SELECT
    rule_id,
    severity,
    COUNT(*) AS alert_count,
    ROUND(AVG(triage_minutes), 1) AS avg_triage_minutes,
    SUM(CASE WHEN sla_breached = 1 THEN 1 ELSE 0 END) AS sla_breaches
FROM alerts
GROUP BY rule_id, severity
ORDER BY alert_count DESC;
```

This query demonstrates grouped analysis, workload review, average response timing, and SLA measurement.

### Active Backlog By Severity

Operational question: what still needs attention?

```sql
SELECT
    severity,
    status,
    COUNT(*) AS alert_count
FROM alerts
WHERE status IN ('open', 'investigating')
GROUP BY severity, status
ORDER BY severity, status;
```

This query demonstrates filtered operational reporting and backlog prioritization.

## What This Shows

These examples show practical SQL applied to business and operational questions. They cover KPI reporting, retention analysis, risk scoring, conditional aggregation, time-based grouping, segmentation, and prioritization.
