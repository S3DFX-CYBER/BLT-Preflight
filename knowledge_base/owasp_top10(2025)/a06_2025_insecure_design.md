# A06:2025 Insecure Design

## Background

Insecure Design slides two spots from #4 to #6 in the ranking as **A02:2025-Security Misconfiguration** and **A03:2025-Software Supply Chain Failures** leapfrog it. 

This category was introduced in 2021. It focuses on risks related to design and architectural flaws, with a strong emphasis on threat modeling, secure design patterns, and reference architectures. This includes flaws in the business logic of an application.

Notable Common Weakness Enumerations (CWEs) include:
- CWE-256: Unprotected Storage of Credentials
- CWE-269: Improper Privilege Management
- CWE-434: Unrestricted Upload of File with Dangerous Type
- CWE-501: Trust Boundary Violation
- CWE-522: Insufficiently Protected Credentials

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 39          | 22.18%             | 1.86%              | 88.76%       | 35.18%       | 6.96                 | 4.05                | 729,882           | 7,647      |

## Description

Insecure design is a broad category representing different weaknesses, expressed as “missing or ineffective control design.” 

**Key distinction**: There is a difference between **insecure design** and **insecure implementation**. An insecure design cannot be fixed by a perfect implementation because the needed security controls were never created.

Three key parts of having a secure design are:
- Gathering Requirements and Resource Management
- Creating a Secure Design
- Having a Secure Development Lifecycle

## How to Prevent

- Establish and use a **secure development lifecycle** with AppSec professionals
- Establish and use a library of **secure design patterns** or paved-road components
- Use **threat modeling** for critical parts of the application (authentication, access control, business logic, key flows)
- Integrate security language and controls into user stories
- Implement plausibility checks at each tier of your application
- Write unit and integration tests to validate that all critical flows are resistant to the threat model
- Segregate tier layers on the system and network layers
- Segregate tenants robustly by design throughout all tiers

## Example Attack Scenarios

**Scenario #1:**  
A credential recovery workflow might include “questions and answers,” which is prohibited by NIST 800-63b. Questions and answers cannot be trusted as evidence of identity. Such functionality should be removed and replaced with a more secure design.

**Scenario #2:**  
A cinema chain allows group booking discounts with a maximum of fifteen attendees. Attackers exploit the business logic flaw and book six hundred seats across all cinemas in a few requests, causing massive financial loss.
