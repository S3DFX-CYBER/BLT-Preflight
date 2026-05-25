# A07:2025 Authentication Failures

## Background

Authentication Failures maintains its position at **#7** with a slight name change to more accurately reflect the 36 CWEs in this category. Despite benefits from standardized frameworks, this category has kept its #7 rank from 2021.

Notable CWEs included are:
- CWE-259: Use of Hard-coded Password
- CWE-297: Improper Validation of Certificate with Host Mismatch
- CWE-287: Improper Authentication
- CWE-384: Session Fixation
- CWE-798: Use of Hard-coded Credentials

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 36          | 15.80%             | 2.92%              | 100.00%      | 37.14%       | 7.69                 | 4.44                | 1,120,673         | 7,147      |

## Description

When an attacker is able to trick a system into recognizing an invalid or incorrect user as legitimate, this vulnerability is present.

The application may be vulnerable if it:

- Permits automated attacks such as credential stuffing or password spraying
- Permits brute force or other automated attacks that are not quickly blocked
- Permits default, weak, or well-known passwords
- Allows users to create new accounts with already known-breached credentials
- Allows use of weak or ineffective credential recovery and forgot-password processes
- Uses plain text, encrypted, or weakly hashed passwords data stores
- Has missing or ineffective multi-factor authentication
- Allows use of weak or ineffective fallbacks if multi-factor authentication is not available
- Exposes session identifiers in the URL or other insecure locations
- Reuses the same session identifier after successful login
- Does not correctly invalidate user sessions or authentication tokens during logout or inactivity
- Does not correctly assert the scope and intended audience of the provided credentials

## How to Prevent

- Implement and enforce **multi-factor authentication** (MFA) wherever possible
- Encourage and enable the use of password managers
- Do not ship or deploy with any default credentials
- Implement weak password checks (test against top 10,000 worst passwords)
- Validate new or changed passwords against known breached credential lists (e.g., Have I Been Pwned)
- Ensure registration, credential recovery, and API pathways are hardened against account enumeration attacks
- Limit or increasingly delay failed login attempts (without creating DoS)
- Use a server-side, secure, built-in session manager that generates new random session IDs with high entropy
- Invalidate sessions after logout, idle, and absolute timeouts
- Ideally, use a well-tested, hardened authentication system and transfer this risk

## Example Attack Scenarios

**Scenario #1:**  
Credential stuffing using lists of known username/password combinations (including password spraying). If the application does not implement proper defenses, attackers can use the application as a password oracle.

**Scenario #2:**  
Continued use of passwords as the sole authentication factor. Organizations are recommended to stop password rotation/complexity requirements (per NIST 800-63) and enforce MFA.

**Scenario #3:**  
Application session timeouts are not implemented correctly. A user on a public computer closes the browser without logging out, allowing the next person to access the still-active session.
