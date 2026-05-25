# A08:2025 Software or Data Integrity Failures

## Background

Software or Data Integrity Failures continues at **#8**, with a slight, clarifying name change from "Software *and* Data Integrity Failures". 

This category is focused on the failure to maintain trust boundaries and verify the integrity of software, code, and data artifacts at a lower level than Software Supply Chain Failures. This category focuses on making assumptions related to software updates and critical data, without verifying integrity.

Notable Common Weakness Enumerations (CWEs) include:
- CWE-829: Inclusion of Functionality from Untrusted Control Sphere
- CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes
- CWE-502: Deserialization of Untrusted Data

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 14          | 8.98%              | 2.75%              | 78.52%       | 45.49%       | 7.11                 | 4.79                | 501,327           | 3,331      |

## Description

Software and data integrity failures relate to code and infrastructure that does not protect against invalid or untrusted code or data being treated as trusted and valid.

**Common examples include:**
- Relying on plugins, libraries, or modules from untrusted sources, repositories, or CDNs
- Insecure CI/CD pipelines that do not verify software integrity
- Applications that download updates without sufficient integrity verification
- Insecure deserialization of untrusted data
- Lack of digital signatures or checksum validation

## How to Prevent

- Use digital signatures or similar mechanisms to verify the software or data is from the expected source and has not been altered
- Ensure libraries and dependencies are only consumed from trusted repositories
- Implement a proper review process for code and configuration changes
- Ensure CI/CD pipelines have proper segregation, configuration, and access control
- Do not accept unsigned or unencrypted serialized data from untrusted clients without integrity checks
- Use Software Bill of Materials (SBOM) and continuous vulnerability scanning

## Example Attack Scenarios

**Scenario #1:**  
A company uses an external service provider for support. They create a DNS mapping `myCompany.SupportProvider.com` to `support.myCompany.com`. This causes authentication cookies to be sent to the support provider, allowing session hijacking.

**Scenario #2:**  
Many IoT devices and routers do not verify firmware updates with signatures. Attackers can distribute malicious firmware updates.

**Scenario #3:**  
A developer downloads a package from an untrusted website instead of the official repository. The package contains malicious code.

**Scenario #4:**  
A React application passes serialized user state between services. An attacker manipulates the serialized data to achieve remote code execution via insecure deserialization.the next number or `next`.
