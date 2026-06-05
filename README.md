![Data Analytics Portfolio](assets/profile/portfolio-header.svg)

# Miguel Angel Torres Mercado

Junior Data Engineer and Data Analyst focused on Python, SQL, data quality, ETL workflows, AWS foundations, and analytical reporting.

I am based in Cartagena, Colombia, with a Systems Engineering background. My portfolio combines reproducible data pipelines, validation controls, analytical modeling, SQL reporting, and business-facing outputs. Security analytics remains a secondary technical area.

## Key Links

- Portfolio site: https://abionit.github.io/AbionitOne/
- Recruiter brief: [RECRUITER_BRIEF.md](RECRUITER_BRIEF.md)
- Primary data project: [Subscription Analytics Lab](https://github.com/Abionit/subscription-analytics-lab)
- AWS architecture: https://github.com/Abionit/subscription-analytics-lab/blob/main/docs/aws_architecture.md
- Data quality evidence: https://github.com/Abionit/subscription-analytics-lab/blob/main/output/data_quality_report.md
- SQL evidence: [SQL_EVIDENCE.md](SQL_EVIDENCE.md)

## Role Direction

- Junior Data Engineer
- Analytics Engineer
- Data Analyst
- BI / Reporting Analyst

## Featured Work

### Subscription Analytics Lab

![Subscription Analytics Lab case study](assets/case-studies/subscription-analytics-lab.svg)

Data engineering and analytics case study for a simulated subscription business.

**Company problem**

Customer, subscription, billing, product usage, and support data arrive from separate sources. The business needs reliable datasets for revenue, retention, customer health, and churn-risk reporting.

**Implemented solution**

- Integrates five source datasets into a customer-month analytical model.
- Runs automated checks for schemas, keys, required values, customer references, and business ranges.
- Stops the pipeline when critical quality rules fail.
- Produces KPI, cohort, churn-risk, segment, and revenue-anomaly outputs.
- Materializes a local SQLite analytical layer with reusable SQL.
- Includes an AWS path using S3, Glue/PySpark, Glue Data Catalog, Athena, and CloudFormation.
- Includes optional Redshift schema and Parquet load scripts.

**Verified evidence**

- Local pipeline executed successfully against `240` customers, `2,351` billing events, `67,706` usage records, and `3,299` support tickets.
- `24/24` data quality checks passed.
- `5/5` automated tests passed.
- CloudFormation template passed `cfn-lint`.
- AWS deployment code is present; cloud execution screenshots remain pending until the stack is run in an AWS account.

**Review path**

- Repository: https://github.com/Abionit/subscription-analytics-lab
- AWS architecture: https://github.com/Abionit/subscription-analytics-lab/blob/main/docs/aws_architecture.md
- Glue job: https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/glue/subscription_etl.py
- Athena queries: https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/athena/portfolio_queries.sql
- Quality report: https://github.com/Abionit/subscription-analytics-lab/blob/main/output/data_quality_report.md

### Wazuh SOC Detection Engineering Lab

![Wazuh SOC Detection Engineering Lab case study](assets/case-studies/wazuh-soc-detection-lab.svg)

Security analytics project built around Wazuh SIEM/XDR, custom detections, MITRE ATT&CK mapping, alert triage, and operational reporting.

- Business problem: security teams need to understand detection coverage, alert priority, and operational risk.
- Evidence: detection catalog, custom rule documentation, triage outputs, alert metrics, and executive reporting.
- Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab

### SOC Home Lab v2

![SOC Home Lab v2 case study](assets/case-studies/soc-home-lab-v2.svg)

Operational analytics case study that turns simulated telemetry into enriched alerts, SQL reports, KPI outputs, and dashboard views.

- Business problem: monitoring teams need visibility into workload, severity, backlog, and response timing.
- Evidence: SQL reporting, alert enrichment, SLA-style metrics, trend analysis, and dashboard outputs.
- Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/soc-home-lab-v2

## Technical Skills

- Data engineering: ETL workflow design, source integration, data validation, data quality gates, analytical modeling
- Programming and data: Python, pandas, SQL, SQLite
- AWS project stack: S3, Glue, PySpark, Glue Data Catalog, Athena, CloudFormation; Redshift integration path
- Reporting: KPI design, CSV and Markdown reports, Streamlit dashboards
- Workflow: GitHub, automated tests, reproducible scripts, technical documentation

## Current Learning

- AWS deployment and operational monitoring for data pipelines
- PySpark transformations and partitioned data processing
- Data warehouse modeling and Redshift
- SQL performance and analytics engineering practices

## Contact

- Portfolio: https://abionit.github.io/AbionitOne/
- LinkedIn: https://linkedin.com/in/miguel-angel-torres-mercado-3b7bb8290
- Email: miguelangeltorresmercado58@gmail.com
- GitHub: https://github.com/Abionit
