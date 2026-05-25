# A04:2025 Cryptographic Failures

## Background

Moving down two positions to #4, this weakness focuses on failures related to the lack of cryptography, insufficiently strong cryptography, leaking of cryptographic keys, and related errors. 

Three of the most common Common Weakness Enumerations (CWEs) in this risk involved the use of a weak pseudo-random number generator: 
- CWE-327: Use of a Broken or Risky Cryptographic Algorithm
- CWE-331: Insufficient Entropy
- CWE-1241: Use of Predictable Algorithm in Random Number Generator
- CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)

## Score Table

| CWEs Mapped | Max Incidence Rate | Avg Incidence Rate | Max Coverage | Avg Coverage | Avg Weighted Exploit | Avg Weighted Impact | Total Occurrences | Total CVEs |
|-------------|--------------------|--------------------|--------------|--------------|----------------------|---------------------|-------------------|------------|
| 32          | 13.77%             | 3.80%              | 100.00%      | 47.74%       | 7.23                 | 3.90                | 1,665,348         | 2,185      |

## Description

Generally speaking, all data in transit should be encrypted at the transport layer. 

Beyond securing the transport layer, it is important to determine what data needs encryption at rest as well as what data needs extra encryption in transit (at the application layer). 

Sensitive data such as passwords, credit card numbers, health records, personal information, and business secrets require extra protection.

**Common issues include:**
- Use of old or weak cryptographic algorithms
- Default, weak, or reused cryptographic keys
- Keys checked into source code repositories
- Missing or weak encryption enforcement
- Improper certificate validation
- Use of insecure modes of operation (e.g., ECB)
- Use of deprecated hash functions (MD5, SHA1)
- Predictable random number generation

## How to Prevent

- Classify data and apply appropriate protection based on sensitivity
- Use strong, up-to-date cryptographic algorithms and protocols (TLS 1.2+ with forward secrecy)
- Store sensitive keys in Hardware Security Modules (HSM) or cloud key management services
- Use strong adaptive password hashing (Argon2, scrypt, bcrypt, PBKDF2)
- Ensure proper key generation, storage, rotation, and management
- Always use authenticated encryption instead of just encryption
- Disable caching for responses containing sensitive data
- Prepare for post-quantum cryptography (PQC) for high-risk systems

## Example Attack Scenarios

**Scenario #1:**  
A site doesn't use or enforce TLS for all pages or supports weak encryption. An attacker monitors network traffic, downgrades connections from HTTPS to HTTP, intercepts requests, and steals the user's session cookie.

**Scenario #2:**  
The password database uses unsalted or simple hashes. An attacker retrieves the database and cracks the passwords using rainbow tables or GPU-based attacks.
