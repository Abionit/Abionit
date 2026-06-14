# Projects

## Business Intelligence And Analytics

### Retail Operations BI Lab

Repository path: [projects/retail-operations-bi-lab](projects/retail-operations-bi-lab)

Business intelligence and data engineering case study for a retail operation that needs reliable sales, inventory, customer, and fulfillment metrics.

- Python ETL workflow
- star schema for Power BI
- DAX measures for revenue, margin, delivery, stockout, and customer KPIs
- SQL queries for business analysis
- data quality checks before modeling
- Power BI report blueprint
- recruiter review guide

Business problem:

Retail teams often work from separate sales, inventory, product, customer, and delivery files. The project builds a clean analytical layer so managers can explain revenue, margin pressure, stockout risk, late deliveries, and customer segment contribution from one model.

Evidence:

- Business case: [projects/retail-operations-bi-lab/docs/business_case.md](projects/retail-operations-bi-lab/docs/business_case.md)
- Power BI blueprint: [projects/retail-operations-bi-lab/powerbi/report_blueprint.md](projects/retail-operations-bi-lab/powerbi/report_blueprint.md)
- DAX measures: [projects/retail-operations-bi-lab/powerbi/measures.dax](projects/retail-operations-bi-lab/powerbi/measures.dax)
- SQL queries: [projects/retail-operations-bi-lab/sql/analytics_queries.sql](projects/retail-operations-bi-lab/sql/analytics_queries.sql)
- Generated summary: [projects/retail-operations-bi-lab/output/business_summary.md](projects/retail-operations-bi-lab/output/business_summary.md)

## Data Engineering

### AWS Subscription Data Pipeline

Repository: https://github.com/Abionit/subscription-analytics-lab

Combines five operational sources into validated analytical datasets for revenue, retention, customer health, and churn-risk reporting.

- Python and pandas ETL workflow
- automated schema, key, null, relationship, and range controls
- customer-month analytical model
- SQLite and reusable SQL
- S3 raw and curated architecture
- AWS Glue PySpark transformation
- Glue Data Catalog and Athena through CloudFormation
- optional Redshift load path
- Streamlit data operations dashboard

Evidence:

- Architecture: https://github.com/Abionit/subscription-analytics-lab/blob/main/docs/aws_architecture.md
- Glue job: https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/glue/subscription_etl.py
- Quality report: https://github.com/Abionit/subscription-analytics-lab/blob/main/output/data_quality_report.md
- Athena queries: https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/athena/portfolio_queries.sql

## Security Operations

### Wazuh SOC Detection Engineering Lab

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab

Detection workflow with custom Wazuh rules, MITRE ATT&CK mapping, alert triage, operational metrics, and executive reporting.

- Detection catalog: https://github.com/Abionit/soc-home-lab/blob/portfolio/wazuh-soc-detection-lab/wazuh-soc-detection-lab/detections/detection_catalog.md
- Custom rules: https://github.com/Abionit/soc-home-lab/blob/portfolio/wazuh-soc-detection-lab/wazuh-soc-detection-lab/config/wazuh/rules/local_soc_rules.xml
- Executive report: https://github.com/Abionit/soc-home-lab/blob/portfolio/wazuh-soc-detection-lab/wazuh-soc-detection-lab/output/executive_report.md

### SOC Operational Analytics

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/soc-home-lab-v2

Transforms simulated telemetry into enriched alerts, backlog metrics, response-time indicators, reusable SQL, and an operational dashboard.

- SQL queries: https://github.com/Abionit/soc-home-lab/blob/portfolio/soc-home-lab-v2/sql/portfolio_queries.sql
- Alert report: https://github.com/Abionit/soc-home-lab/blob/portfolio/soc-home-lab-v2/output/alerts_report.md
- Evidence gallery: https://github.com/Abionit/soc-home-lab/blob/portfolio/soc-home-lab-v2/evidence/v2/README.md

## Security Research

### Controlled Lab Write-Ups

Repository: https://github.com/Abionit/writeups

Technical documentation covering controlled Hack The Box and PortSwigger environments, with emphasis on methodology, evidence, impact, and remediation context.
