# Recruiter Brief

## Profile Summary

Early-career data professional from Cartagena, Colombia, with a Systems Engineering background and practical projects in data pipelines, SQL, data quality, analytical modeling, and reporting.

The primary project integrates five operational datasets, applies automated quality controls, builds a reusable analytical layer, and includes a deployment-ready AWS architecture using S3, Glue/PySpark, Glue Data Catalog, Athena, CloudFormation, and an optional Redshift path.

## Target Roles

- Junior Data Engineer
- Analytics Engineer
- Data Analyst
- BI / Reporting Analyst

## Strongest Project

[Subscription Analytics Lab](https://github.com/Abionit/subscription-analytics-lab)

The project addresses a clear business problem: customer, billing, usage, subscription, and support data are separated, while reporting teams need trusted datasets for revenue, retention, and churn analysis.

Evidence available in the repository:

- Python pipeline integrating five data sources
- automated schema, key, foreign-key, completeness, and range checks
- customer-month analytical model
- SQLite and reusable SQL queries
- S3 raw and curated architecture
- AWS Glue PySpark job
- Glue Data Catalog crawler and Athena workgroup through CloudFormation
- Athena analytical queries
- optional Redshift schema and Parquet load commands
- unit tests and generated quality report

Verified locally:

- 240 customers
- 2,351 billing events
- 67,706 product-usage records
- 3,299 support tickets
- 24 of 24 quality checks passed
- 5 of 5 automated tests passed
- CloudFormation template passed cfn-lint

The AWS implementation is present as code. It should only be described as deployed after running it in an AWS account and adding execution evidence.

## Review Sequence

1. [Primary repository](https://github.com/Abionit/subscription-analytics-lab)
2. [AWS architecture](https://github.com/Abionit/subscription-analytics-lab/blob/main/docs/aws_architecture.md)
3. [Data quality report](https://github.com/Abionit/subscription-analytics-lab/blob/main/output/data_quality_report.md)
4. [Glue PySpark job](https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/glue/subscription_etl.py)
5. [Athena queries](https://github.com/Abionit/subscription-analytics-lab/blob/main/aws/athena/portfolio_queries.sql)
6. [SQL evidence](SQL_EVIDENCE.md)

## Interview Discussion Areas

- Why the pipeline uses raw and curated S3 zones
- How quality gates prevent invalid data from reaching analytical tables
- Why Parquet partitioning reduces Athena scan cost
- How five operational sources are joined into a customer-month model
- When Athena is sufficient and when Redshift becomes useful
- How the same pipeline can run locally for development and in Glue for cloud processing

## Contact

- Portfolio: https://abionit.github.io/AbionitOne/
- LinkedIn: https://linkedin.com/in/miguel-angel-torres-mercado-3b7bb8290
- GitHub: https://github.com/Abionit
- Email: miguelangeltorresmercado58@gmail.com
