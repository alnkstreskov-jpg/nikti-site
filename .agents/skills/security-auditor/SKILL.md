---
name: Security Auditor
description: Ensures basic web security practices. Triggers when handling passwords, authentication, or user input.
---
# Security Auditor

When writing features that handle sensitive data or user input:
- Validate and sanitize all user inputs to prevent injection attacks.
- Ensure passwords are checked for basic strength requirements (length, complexity).
- Prevent Cross-Site Scripting (XSS) by properly escaping outputs.
- Enforce basic security headers and advise on secure data storage practices (e.g., proper hashing).
