# A01:2025 Broken Access Control

## Background

Maintaining its position at #1 in the Top Ten, **100% of the applications tested** were found to have some form of broken access control. 

Notable CWEs included are:
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
- CWE-201: Exposure of Sensitive Information Through Sent Data
- CWE-918: Server-Side Request Forgery (SSRF)
- CWE-352: Cross-Site Request Forgery (CSRF)

This category has the highest number of occurrences in the contributed data and the second highest number of related CVEs.

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 40          | 20.15%             | 3.74%              | 100.00%      | 42.93%       | 7.04                 | 3.84                | 1,839,701         | 32,654     |

## Description

Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification or destruction of all data, or performing a business function outside the user's limits.

**Common access control vulnerabilities include:**

- Violation of the principle of least privilege (deny by default)
- Bypassing access control checks by modifying the URL, internal state, or using attack tools
- Insecure Direct Object References (IDOR)
- Missing access controls on APIs (especially POST, PUT, DELETE)
- Elevation of privilege
- Metadata manipulation (e.g., tampering with JWTs, cookies)
- CORS misconfiguration
- Force browsing to privileged pages

## How to Prevent

Access control is only effective when implemented in **trusted server-side code** or serverless APIs.

**Best Practices:**

- Deny by default (except for public resources)
- Implement access control mechanisms once and reuse them
- Enforce record ownership in domain models
- Disable web server directory listing and protect metadata files
- Log access control failures and alert on repeated attempts
- Implement rate limiting on APIs
- Use short-lived stateless tokens (JWTs) and follow OAuth standards for revocation
- Use well-established libraries and frameworks for access control

Developers and QA should include functional access control tests in their test suites.

## Example Attack Scenarios

**Scenario #1:**  
An application uses unverified data in an SQL call:

```sql
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery();
```
An attacker modifies the ```acct``` parameter to access any user's account.
## Example URL Attack
https://example.com/app/accountInfo?acct=notmyacct
