# A05:2025 Injection

## Background

Injection falls two spots from #3 to #5 in the ranking, maintaining its position relative to A04:2025-Cryptographic Failures and A06:2025-Insecure Design. 

Injection is one of the most tested categories with **100% of applications tested** for some form of injection. It had the greatest number of CVEs for any category, with **37 CWEs** in this category.

Injection includes Cross-site Scripting (high frequency/low impact) with more than 30k CVEs and SQL Injection (low frequency/high impact) with more than 14k CVEs.

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 37          | 13.77%             | 3.08%              | 100.00%      | 42.93%       | 7.15                 | 4.32                | 1,404,249         | 62,445     |

## Description

An **injection vulnerability** is an application flaw that allows untrusted user input to be sent to an interpreter (e.g. a browser, database, the command line) and causes the interpreter to execute parts of that input as commands.

An application is vulnerable when:
- User-supplied data is not validated, filtered, or sanitized by the application.
- Dynamic queries or non-parameterized calls without context-aware escaping are used directly in the interpreter.
- Unsanitized data is used within object-relational mapping (ORM) search parameters.
- Potentially hostile data is directly used or concatenated in dynamic queries, commands, or stored procedures.

**Common injection types include:**
- SQL Injection
- NoSQL Injection
- OS Command Injection
- Cross-Site Scripting (XSS)
- LDAP Injection
- Expression Language (EL) / OGNL Injection

## How to Prevent

The best defense is to **keep data separate from commands and queries**:

- Use a safe API that avoids using the interpreter entirely, provides a parameterized interface, or uses Object Relational Mapping Tools (ORMs).
- Use positive server-side input validation.
- For any residual dynamic queries, escape special characters using the specific escape syntax for that interpreter.
- Implement proper output encoding (especially for XSS).

**Note:** Even parameterized queries can be vulnerable if stored procedures concatenate input unsafely.

## Example Attack Scenarios

**Scenario #1:**  
An application uses untrusted data in the construction of the following vulnerable SQL call:

```sql
String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";
