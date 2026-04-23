# Portfolio Case Studies

These case studies represent the strongest portfolio evidence for entry-level Data Analyst, BI Analyst, Reporting Analyst, and analytics-oriented roles.

For a focused review of SQL work, see [SQL_EVIDENCE.md](SQL_EVIDENCE.md).

## Case Study 1: Subscription Analytics Lab

![Subscription Analytics Lab case study](assets/case-studies/subscription-analytics-lab.svg)

### Business Question

Which signals help identify revenue risk, retention pressure, and customer health issues early in a subscription business?

### Analytical Approach

The project builds a practical analytics workflow around synthetic subscription data. It starts with customer, billing, usage, and support data, then creates a customer-month analytical layer for recurring revenue and retention analysis.

### Tools

- Python
- SQL
- SQLite
- Streamlit
- CSV and Markdown reporting

### Workflow

1. Generate synthetic customer, billing, usage, and support data.
2. Build a customer-month analytical layer.
3. Calculate business KPIs such as MRR, ARPA, logo churn, and net revenue retention.
4. Analyze cohort retention and segment performance.
5. Score churn risk using usage, payment, support, CSAT, and contraction signals.
6. Export outputs and review results through a dashboard.

### Key Outputs

- Monthly KPI series
- Cohort retention table
- Segment-level summary
- Churn risk watchlist
- Revenue anomaly report
- Streamlit dashboard
- SQL query layer

### What It Demonstrates

This project demonstrates the ability to move from raw data to a structured analytical model, then communicate the results through reports and dashboards. It shows practical SQL, Python, KPI design, and business analysis skills.

### Links

- Repository: https://github.com/Abionit/subscription-analytics-lab
- SQL queries: https://github.com/Abionit/subscription-analytics-lab/blob/main/sql/portfolio_queries.sql
- Sample report: https://github.com/Abionit/subscription-analytics-lab/blob/main/output/subscription_analytics_report.md

## Case Study 2: SOC Home Lab v2

![SOC Home Lab v2 case study](assets/case-studies/soc-home-lab-v2.svg)

### Business Question

How can a small SOC workflow turn simulated telemetry into enriched alerts, operational metrics, and reusable reports?

### Analytical Approach

The project uses security telemetry as an operational analytics problem. Events are generated, detection rules produce alerts, and the results are enriched with severity, ownership, status, timing, and SLA context before being reviewed through SQL and a dashboard.

### Tools

- Python
- SQL
- SQLite
- Streamlit
- Markdown reporting

### Workflow

1. Generate simulated security telemetry.
2. Apply detection rules to identify suspicious behavior.
3. Enrich alerts with context such as severity, ownership, status, timing, and SLA flags.
4. Export KPI and alert outputs.
5. Query the results with SQL.
6. Review trends, severity distribution, triage status, and alert tables in a dashboard.

### Key Outputs

- Enriched alerts table
- Alert KPI summary
- Rule summary
- Alert trend output
- Markdown report
- SQLite analytics layer
- Streamlit dashboard

### What It Demonstrates

This project shows how data analysis can support security operations. It connects detection logic, triage metrics, SQL reporting, and dashboard communication in one workflow.

### Links

- Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/soc-home-lab-v2
- SQL queries: https://github.com/Abionit/soc-home-lab/blob/portfolio/soc-home-lab-v2/sql/portfolio_queries.sql
- Sample report: https://github.com/Abionit/soc-home-lab/blob/portfolio/soc-home-lab-v2/output/alerts_report.md

## Portfolio Positioning

These projects are designed to support entry-level roles involving:

- Data analysis
- BI and reporting
- SQL-heavy analysis
- Dashboarding
- Operational analytics
- Security analytics as a secondary differentiator
