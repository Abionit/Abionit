# Recruiter Brief

## Profile Summary

Systems Engineer based in Cartagena, Colombia, focused on Data Engineering, cloud data pipelines, data quality, SQL, and Security Operations analytics.

The portfolio combines data integration, automated validation, analytical modeling, cloud architecture, SIEM detection work, alert triage, and operational reporting. Each project is organized around a practical company problem and includes code, documentation, outputs, and reviewable evidence.

## Professional Focus

- Data Engineer
- Analytics Engineer
- Cloud Data Engineering
- Security Analytics
- SOC Operations and Detection Engineering

## Primary Data Engineering Project

[Subscription Analytics Lab](https://github.com/Abionit/subscription-analytics-lab)

The project addresses a common data problem: customer, subscription, billing, product usage, and support information is separated across different sources, while reporting teams need reliable datasets for revenue, retention, customer health, and churn analysis.

Evidence available:

- Python pipeline integrating five source datasets
- automated schema, key, foreign-key, completeness, and range controls
- customer-month analytical model
- SQLite and reusable SQL queries
- S3 raw and curated data architecture
- AWS Glue PySpark transformation
- Glue Data Catalog crawler and Athena workgroup through CloudFormation
- Athena analytical queries
- optional Redshift schema and Parquet load commands
- unit tests and generated quality reports

Verified locally:

- `240` customers
- `2,351` billing events
- `67,706` product-usage records
- `3,299` support tickets
- `24/24` quality checks passed
- `5/5` automated tests passed
- CloudFormation passed `cfn-lint`

The AWS implementation is published as code. Cloud execution should only be claimed after deployment and the addition of real AWS evidence.

## Security Operations Projects

### Wazuh SOC Detection Engineering Lab

Demonstrates custom Wazuh detections, MITRE ATT&CK mapping, alert triage, operational metrics, and executive security reporting.

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab

### SOC Home Lab v2

Demonstrates event enrichment, SQL-based alert analysis, backlog review, rule performance, SLA-style metrics, and dashboard reporting.

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/soc-home-lab-v2

## Review Sequence

1. [Data engineering repository](https://github.com/Abionit/subscription-analytics-lab)
2. [AWS architecture](https://github.com/Abionit/subscription-analytics-lab/blob/main/docs/aws_architecture.md)
3. [Data quality report](https://github.com/Abionit/subscription-analytics-lab/blob/main/output/data_quality_report.md)
4. [Glue PySpark job](https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/glue/subscription_etl.py)
5. [Athena queries](https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/athena/portfolio_queries.sql)
6. [Wazuh SOC project](https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab)
7. [SQL evidence](SQL_EVIDENCE.md)

## Interview Discussion Areas

- Raw and curated S3 data zones
- Data quality gates and pipeline failure behavior
- Parquet partitioning and Athena scan efficiency
- Multi-source integration into a customer-month model
- Athena and Redshift use cases
- Local development and Glue cloud execution
- Wazuh detection logic and MITRE ATT&CK mapping
- SOC alert prioritization and operational metrics

## Contact

- Portfolio: https://abionit.github.io/AbionitOne/
- LinkedIn: https://linkedin.com/in/miguel-angel-torres-mercado-3b7bb8290
- GitHub: https://github.com/Abionit
- Email: miguelangeltorresmercado58@gmail.com
