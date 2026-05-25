# A02:2025 Security Misconfiguration

## Background

Moving up from #5 in the previous edition, **100% of the applications tested** were found to have some form of misconfiguration, with an average incidence rate of 3.00%, and over 719k occurrences. 

Notable CWEs included are:
- CWE-16: Configuration
- CWE-611: Improper Restriction of XML External Entity Reference (XXE)

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 16          | 27.70%             | 3.00%              | 100.00%      | 52.35%       | 7.96                 | 3.97                | 719,084           | 1,375      |

## Description

Security misconfiguration is when a system, application, or cloud service is set up incorrectly from a security perspective, creating vulnerabilities.

The application might be vulnerable if:

- The security settings in the application servers, application frameworks (e.g., Struts, Spring, ASP.NET), libraries, databases, etc., are not set to secure values.
- The server does not send security headers or directives, or they are not set to secure values.
- Error handling reveals stack traces or sensitive information.
- Default accounts and passwords are still enabled.
- Unnecessary features, components, or sample applications are left in production.
- Cloud storage permissions are overly permissive.

Without a concerted, repeatable application security configuration hardening process, systems are at a higher risk.

## How to Prevent

Secure installation processes should be implemented, including:

- A repeatable hardening process enabling fast and easy deployment of a properly locked-down environment. Development, QA, and production environments should be configured identically (except for credentials).
- A minimal platform without any unnecessary features, components, documentation, or samples. Remove unused features and frameworks.
- Automated processes to verify the effectiveness of configurations and settings across all environments.
- Proactive interception of excessive error messages.
- Use identity federation, short-lived credentials, or role-based access instead of embedding static secrets.
- Regular automated scans for misconfigurations.

## Example Attack Scenarios

**Scenario #1:**  
The application server comes with sample applications not removed from the production server. These sample applications have known security flaws. One of them is the admin console with default credentials still active. An attacker logs in and takes over the server.

**Scenario #2:**  
Directory listing is not disabled on the server. An attacker lists directories and downloads compiled Java classes, then decompiles them to discover severe access control flaws in the application.

**Scenario #3:**  
Cloud storage buckets are configured with public access, allowing anyone to read sensitive data.
