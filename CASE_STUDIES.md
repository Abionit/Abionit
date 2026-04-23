# Portfolio Case Studies

These case studies represent the strongest portfolio evidence for entry-level Data Analyst, BI Analyst, Reporting Analyst, security analytics, and analytics-oriented roles.

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

### Key Outputs

- Monthly KPI series
- Cohort retention table
- Segment-level summary
- Churn risk watchlist
- Revenue anomaly report
- Streamlit dashboard
- SQL query layer

### Links

- Repository: https://github.com/Abionit/subscription-analytics-lab
- SQL queries: https://github.com/Abionit/subscription-analytics-lab/blob/main/sql/portfolio_queries.sql
- Sample report: https://github.com/Abionit/subscription-analytics-lab/blob/main/output/subscription_analytics_report.md

## Case Study 2: Wazuh SOC Detection Engineering Lab

![Wazuh SOC Detection Engineering Lab case study](assets/case-studies/wazuh-soc-detection-lab.svg)

### Operational Question

How can a SOC lab use Wazuh to turn controlled security events into mapped detections, triage decisions, and reviewable reporting?

### Analytical Approach

The project uses Wazuh as the SIEM/XDR layer and adds custom detection rules, controlled event generation, MITRE ATT&CK mapping, triage outputs, and alert analytics. The workflow is designed to show both SOC detection engineering and data-driven reporting.

### Tools

- Wazuh
- Docker
- Python
- SQLite
- Streamlit
- Markdown and CSV reporting

### Key Outputs

- Custom Wazuh detection rules
- MITRE ATT&CK detection catalog
- Wazuh Docker deployment runbook
- Generated lab events
- Alert metrics CSV
- Triage queue CSV
- Executive SOC report
- Optional Streamlit dashboard

### Links

- Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab
- Detection catalog: https://github.com/Abionit/soc-home-lab/blob/portfolio/wazuh-soc-detection-lab/wazuh-soc-detection-lab/detections/detection_catalog.md
- Custom rules: https://github.com/Abionit/soc-home-lab/blob/portfolio/wazuh-soc-detection-lab/wazuh-soc-detection-lab/config/wazuh/rules/local_soc_rules.xml
- Executive report: https://github.com/Abionit/soc-home-lab/blob/portfolio/wazuh-soc-detection-lab/wazuh-soc-detection-lab/output/executive_report.md

## Case Study 3: SOC Home Lab v2

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

### Key Outputs

- Enriched alerts table
- Alert KPI summary
- Rule summary
- Alert trend output
- Markdown report
- SQLite analytics layer
- Streamlit dashboard

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
- SOC analyst and junior detection engineering foundations
