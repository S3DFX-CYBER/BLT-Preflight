# A09:2025 Security Logging and Alerting Failures

## Background

Security Logging & Alerting Failures retains its position at **#9**. This category has a slight name change to emphasize the alerting function needed to induce action on relevant logging events. 

This category will always be underrepresented in the data, and for the third time voted into a position in the list from the community survey participants. This category is incredibly difficult to test for, and has minimal representation in the CVE/CVSS data (only 723 CVEs); but can be very impactful for visibility and incident alerting and forensics.

Notable CWEs included are:
- CWE-117: Improper Output Neutralization for Logs
- CWE-532: Insertion of Sensitive Information into Log File
- CWE-778: Insufficient Logging

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 5           | 11.33%             | 3.91%              | 85.96%       | 46.48%       | 7.19                 | 2.65                | 260,288           | 723        |

## Description

Without logging and monitoring, attacks and breaches cannot be detected, and without alerting it is very difficult to respond quickly and effectively during a security incident.

The application may be vulnerable if:
- Auditable events (logins, failed logins, high-value transactions) are not logged or logged inconsistently
- Warnings and errors generate no, inadequate, or unclear log messages
- Logs are not monitored for suspicious activity
- Logs are only stored locally without proper backup
- Appropriate alerting thresholds and response processes are missing
- Penetration testing and DAST scans do not trigger alerts
- Sensitive information is logged (e.g., PII, credentials)
- Logs are vulnerable to injection attacks due to improper encoding

## How to Prevent

- Ensure all login, access control, and input validation failures are logged with sufficient context
- Log both successful and failed security events
- Use a standardized log format that log management tools can consume
- Protect log integrity (tamper-proof storage)
- Implement effective monitoring and alerting with proper thresholds
- Create playbooks for the Security Operations Center (SOC)
- Use honeytokens to detect attackers with low false positives
- Establish an incident response plan (e.g., NIST 800-61)

## Example Attack Scenarios

**Scenario #1:**  
A children's health plan provider's website suffered a breach affecting 3.5 million records. Due to lack of logging and monitoring, the breach went undetected for over 7 years.

**Scenario #2:**  
A major Indian airline suffered a breach exposing millions of passengers' data. The breach was only discovered when the cloud hosting provider notified them.
