# A10:2025 Mishandling of Exceptional Conditions

## Background

Mishandling of Exceptional Conditions is a **new category for 2025**. This category contains 24 CWEs and focuses on improper error handling, logical errors, failing open, and other related scenarios stemming from abnormal conditions a system may encounter.

This category has some CWEs that were previously associated with poor code quality. That was too general; this more specific category provides better guidance.

Notable CWEs included:
- CWE-209: Generation of Error Message Containing Sensitive Information
- CWE-234: Failure to Handle Missing Parameter
- CWE-274: Improper Handling of Insufficient Privileges
- CWE-476: NULL Pointer Dereference
- CWE-636: Not Failing Securely ('Failing Open')

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 24          | 20.67%             | 2.95%              | 100.00%      | 37.95%       | 7.11                 | 3.81                | 769,581           | 3,416      |

## Description

Mishandling exceptional conditions in software happens when programs fail to prevent, detect, and respond to unusual and unpredictable situations. This leads to crashes, unexpected behavior, and sometimes security vulnerabilities.

Exceptional conditions can be caused by:
- Missing, poor, or incomplete input validation
- Late or high-level error handling instead of handling at the point of occurrence
- Unexpected environmental states (memory, privilege, network issues)
- Inconsistent exception handling
- Exceptions that are not handled at all

Any time an application is unsure of its next instruction, an exceptional condition has been mishandled.

## How to Prevent

- Plan for exceptional conditions (expect the worst)
- Catch every possible system error **at the place where it occurs**
- Handle it meaningfully: throw a user-friendly error, log the event, and alert if necessary
- Implement a **global exception handler**
- Use **centralized** error handling, logging, monitoring, and alerting
- Fail closed (rollback transactions completely) instead of failing open
- Add rate limiting, resource quotas, and throttling
- Perform strict input validation and sanitization
- Conduct threat modeling and secure design reviews

## Example Attack Scenarios

**Scenario #1:**  
Resource exhaustion (DoS) — The application catches exceptions when files are uploaded but doesn’t properly release resources. Each exception leaves resources locked until the system runs out.

**Scenario #2:**  
Sensitive data exposure — Database errors reveal full system stack traces or sensitive information to the user. Attackers use this information to craft better attacks (e.g., SQL injection).

**Scenario #3:**  
State corruption in financial transactions — An attacker interrupts a multi-step transaction (debit → credit → log). If the system doesn’t properly rollback on error, the attacker can drain accounts or duplicate transactions.
