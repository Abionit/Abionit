# Project Business Value

## AWS Subscription Data Pipeline

Repository: https://github.com/Abionit/subscription-analytics-lab

**Company problem**

Customer, subscription, billing, product usage, and support data arrives from separate operational sources. Without a controlled integration process, reporting teams can receive incomplete, duplicated, or inconsistent information.

**Solution**

- integrates five source datasets
- validates schemas, keys, required fields, customer relationships, and business ranges
- stops processing when critical quality rules fail
- builds customer-month and KPI datasets
- stores local analytical tables in SQLite
- defines S3 raw and curated zones
- transforms data with AWS Glue and PySpark
- exposes curated data through Glue Data Catalog and Athena
- provides an optional Redshift load path

**Business use**

- recurring revenue and retention reporting
- customer-risk prioritization
- trusted datasets for analytics and BI
- traceable quality checks before publication
- lower-cost SQL analysis over partitioned Parquet in S3

## Wazuh SOC Detection Engineering Lab

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab

**Company problem**

Security teams need detection coverage, prioritization, and reporting instead of isolated raw events.

**Solution**

- custom Wazuh detection rules
- MITRE ATT&CK mapping
- controlled validation events
- triage queue and severity context
- operational security metrics
- executive and technical reporting

**Business use**

- detection coverage review
- alert prioritization
- rule validation and tuning
- SOC workload reporting
- communication of security risk to technical and management teams

## SOC Operational Analytics

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/soc-home-lab-v2

**Company problem**

A monitoring team needs visibility into alert volume, severity, backlog, ownership, rule activity, and response times.

**Solution**

- event generation and rule-based detection
- alert enrichment with asset, user, status, and SLA context
- SQL queries for trends, backlog, and rule performance
- KPI exports and operational dashboard

**Business use**

- daily queue review
- backlog and SLA monitoring
- workload distribution
- rule-performance analysis
- operational reporting for SOC leads
