# A03:2025 Software Supply Chain Failures

## Background

This was top-ranked in the Top 10 community survey with exactly **50%** of respondents ranking it #1. 

Since initially appearing in the 2013 Top 10 as "A9 – Using Components with Known Vulnerabilities", the risk has grown in scope to include all supply chain failures. 

Despite this increased scope, supply chain failures continue to be a challenge to identify with only **11 CVEs** having the related CWEs. However, when tested, this category has the **highest average incidence rate at 5.72%**.

Relevant CWEs:
- CWE-477: Use of Obsolete Function
- CWE-1104: Use of Unmaintained Third Party Components
- CWE-1329: Reliance on Component That is Not Updateable
- CWE-1395: Dependency on Vulnerable Third-Party Component

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 6           | 9.56%              | 5.72%              | 65.42%       | 27.47%       | 8.17                 | 5.23                | 215,248           | 11         |

## Description

Software supply chain failures are breakdowns or other compromises in the process of building, distributing, or updating software. They are often caused by vulnerabilities or malicious changes in third-party code, tools, or other dependencies.

You are likely vulnerable if:
- You do not carefully track versions of all components (direct + transitive dependencies)
- Software/components are vulnerable, unsupported, or out of date
- You do not regularly scan for vulnerabilities or subscribe to security bulletins
- There is no proper change management process for your supply chain
- You use components from untrusted sources
- Your CI/CD pipeline has weaker security than the systems it builds

## How to Prevent

- Establish a strong **patch management process**
- Centrally generate and manage **Software Bill of Materials (SBOM)**
- Track both direct and transitive dependencies
- Remove unused dependencies and features
- Continuously monitor for vulnerabilities using tools like OWASP Dependency-Check, OWASP Dependency-Track, etc.
- Only obtain components from official trusted sources (prefer signed packages)
- Regularly update CI/CD pipelines, IDEs, and developer tooling
- Implement separation of duties in your supply chain
- Use staged rollouts / canary deployments when updating dependencies

## Example Attack Scenarios

**Scenario #1:**  
A trusted vendor is compromised with malware (e.g., **SolarWinds 2019** supply chain attack), leading to compromise of ~18,000 organizations when they upgraded.

**Scenario #2:**  
A trusted vendor is compromised such that it behaves maliciously only under specific conditions (e.g., **Bybit 2025** wallet software attack resulting in $1.5 billion theft).

**Scenario #3:**  
The **Shai-Hulud** supply chain attack (2025) — the first successful self-propagating npm worm that infected over 500 package versions.
