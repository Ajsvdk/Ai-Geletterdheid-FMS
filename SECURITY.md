# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| latest   | :white_check_mark: |

## Reporting a Vulnerability

Please report (suspected) security vulnerabilities to A. van der Kuil. You will receive a response from us within 48 hours. If the issue is confirmed, we will release a patch as soon as possible depending on complexity.

## Security Measures

This project implements several security measures:

1. **Content Security Policy (CSP)**
   - Strict control over which resources can be loaded
   - CSP violation reporting enabled
   - Report-Only mode for testing new policies

2. **HTTPS Enforcement**
   - All traffic is forced over HTTPS
   - HSTS preloading enabled
   - Secure TLS configuration

3. **Security Headers**
   - X-Content-Type-Options: nosniff
   - X-Frame-Options: DENY
   - Referrer-Policy: strict-origin-when-cross-origin
   - Permissions-Policy restrictions
   - Strict Transport Security (HSTS)

4. **Automated Security**
   - Weekly security scans
   - Dependency vulnerability checking
   - OWASP ZAP scanning
   - CodeQL analysis

5. **Access Control**
   - Strict permissions model
   - Regular security updates
   - Protected branches

## Security Best Practices

When contributing to this project, please:

1. Never commit sensitive information
2. Keep dependencies updated
3. Follow secure coding practices
4. Report security issues privately
5. Use strong authentication

## Contact

For security issues, please contact A. van der Kuil directly rather than opening a public issue. 