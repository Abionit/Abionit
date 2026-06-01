# Project Business Value

This page explains the business purpose behind each portfolio project. The goal is to make the projects easier to review from a hiring perspective: what problem they represent, how they could be used inside a company, and what kind of analytical work they demonstrate.

## Summary

| Project | Best fit | Business value |
| --- | --- | --- |
| Subscription Analytics Lab | Data Analyst, BI Analyst, Reporting Analyst | Revenue, retention, churn risk, customer health, and KPI reporting for a subscription business. |
| Wazuh SOC Detection Engineering Lab | Security Analytics Analyst, Junior SOC Analyst | Detection coverage, alert triage, operational security metrics, and executive reporting. |
| SOC Home Lab v2 | Operations Analyst, Reporting Analyst, Security Analytics | Alert workload, backlog review, SLA-style metrics, and rule-performance reporting. |

## Subscription Analytics Lab

Repository: https://github.com/Abionit/subscription-analytics-lab

### What The Project Represents

This project models the kind of reporting workflow a subscription business would need to understand revenue, retention, customer health, and churn risk. It is built around recurring metrics rather than one-time analysis, which makes it closer to the kind of work expected in data, BI, and reporting roles.

### Company Problem

A subscription company needs to know whether revenue is growing, which customers are at risk, how retention changes over time, and which segments deserve attention. If those signals are scattered across separate files or reports, teams can miss churn risk or react too late.

### How It Could Be Used In A Company

- Monthly KPI review for MRR, ARPA, active customers, churn, and retention.
- Customer success prioritization through a churn-risk watchlist.
- Cohort retention analysis to compare customer behavior over time.
- Segment and regional review to identify weaker or stronger groups.
- Revenue anomaly checks to flag unusual movement in accounts or periods.

### Evidence In The Project

- Python pipeline for generating and preparing analytical data.
- SQLite layer and reusable SQL queries for business review.
- KPI exports, cohort outputs, churn watchlist, segment summaries, and anomaly outputs.
- Markdown report designed to summarize findings without requiring a local setup.
- Streamlit dashboard path for interactive review.

### Value For A Data Analyst Role

This is the strongest project for Data Analyst and BI roles because it shows the full analytical path: define the business questions, prepare the data, calculate useful metrics, create SQL outputs, and explain the results in a way that a team could review.

## Wazuh SOC Detection Engineering Lab

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/wazuh-soc-detection-lab

### What The Project Represents

This project models a small security analytics workflow using Wazuh SIEM/XDR concepts. It focuses on custom detections, MITRE ATT&CK mapping, alert triage, and operational reporting.

### Company Problem

Security teams need more than raw alerts. They need to understand which detections exist, what each alert means, which events deserve priority, and how to report activity to technical reviewers or leadership.

### How It Could Be Used In A Company

- Detection coverage review for common security scenarios.
- Alert triage support using severity, rule context, and MITRE mapping.
- Operational reporting around alert volume and critical detections.
- Documentation of detection logic for review and maintenance.
- Executive-style summaries that explain risk and activity without relying only on raw logs.

### Evidence In The Project

- Custom Wazuh rule documentation.
- Detection catalog mapped to MITRE ATT&CK techniques.
- Alert analytics outputs and triage queue structure.
- Executive report and supporting evidence files.
- Python and SQLite-based reporting workflow.

### Value For A Data Or Security Analytics Role

This project is a secondary differentiator. It keeps the portfolio connected to analytics while showing security context: alert prioritization, operational metrics, detection documentation, and evidence-based reporting.

## SOC Home Lab v2

Repository: https://github.com/Abionit/soc-home-lab/tree/portfolio/soc-home-lab-v2

### What The Project Represents

This project is a compact operations analytics case study for alert telemetry. It turns simulated events into enriched alerts, KPI outputs, SQL reports, and dashboard views.

### Company Problem

Monitoring teams need to understand workload and priority: how many alerts are open, which alerts are critical, where backlog is building, which rules generate the most activity, and whether response timing is acceptable.

### How It Could Be Used In A Company

- Daily or weekly queue review by severity and status.
- Backlog monitoring for open and investigating alerts.
- Rule-performance review to identify high-volume or high-impact detections.
- SLA-style reporting for triage and resolution timing.
- Dashboard views for analysts, team leads, or operations review.

### Evidence In The Project

- Event generation and alert enrichment workflow.
- SQL queries for alert KPIs, trends, rule summaries, and backlog review.
- CSV outputs for KPI and rule-level reporting.
- Markdown report for fast review.
- Evidence gallery with representative dashboard and output views.

### Value For An Operations Or Reporting Role

This project shows how operational data can be structured into useful reporting. The value is not only in the security context, but in the analysis pattern: define the queue, enrich the data, calculate workload metrics, and present the status clearly.

## Portfolio Positioning

The main direction of the portfolio is data analysis and reporting. The security projects are included because they show the same analytical habits in a more technical environment.

- Subscription Analytics Lab is the primary project for Data Analyst and BI roles.
- Wazuh SOC Detection Engineering Lab adds security analytics depth.
- SOC Home Lab v2 shows operational reporting and prioritization.

Across the projects, the common pattern is consistent: structure the data, define useful metrics, create reusable analysis, and communicate the result clearly.
