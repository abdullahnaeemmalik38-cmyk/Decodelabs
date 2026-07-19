# Password Strength Checker

## Overview

This project was developed during my internship at DecodeLabs. The primary objective was to build a Password Strength Checker capable of evaluating password security using modern security principles rather than relying solely on simple length requirements.

In addition to the required functionality, I extended the project by implementing a secure password generator, password breach detection, entropy-based strength analysis, and detailed security reporting.

The application is built as a web-based solution using Flask, HTML, CSS, and JavaScript.

---

## Features

### Password Strength Analysis

The system evaluates passwords using multiple security factors:

* Password length validation
* Uppercase character detection
* Lowercase character detection
* Numeric digit detection
* Symbol detection
* Unicode character support
* Sequential pattern detection
* Common password detection
* Entropy-based security evaluation
* Brute-force resistance estimation

Passwords are classified into the following categories:

* Weak
* Medium
* Strong
* Very Strong

Any password shorter than 8 characters is automatically classified as weak and rejected from advanced analysis.

---

### Entropy-Based Evaluation

The application calculates password entropy using both ASCII and Unicode character spaces to provide a more realistic assessment of password strength.

The entropy score is used to estimate:

* Password unpredictability
* Resistance against brute-force attacks
* Estimated cracking time

---

### Security Analysis

For passwords rated Medium or higher, the system generates a detailed security report including:

* Password length
* Character categories used
* Entropy score (bits)
* Estimated crack time
* Security observations and recommendations

For passwords classified as Weak, advanced entropy and security analysis is intentionally skipped.

---

### Breach Detection

The application integrates password breach checking using:

* hashlib
* requests

The system queries breach data from Have I Been Pwned using a privacy-preserving approach and reports:

* Whether the password has appeared in known data breaches
* Number of times the password has been exposed

This helps users avoid passwords that are already publicly compromised.

---

### Secure Password Generator

An additional feature beyond the internship requirements is a secure password generator.

The generator creates strong passwords using:

* Uppercase letters
* Lowercase letters
* Digits
* Symbols

Randomness is generated using cryptographically secure methods to improve password security.

---

### Security Enhancements

The application incorporates several security-focused techniques:

* HMAC-based processing to help reduce information leakage
* Linear-time password validation (O(n))
* Unicode-aware character analysis
* Secure password handling practices
* Modern hashing and security libraries

---

## Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Python Libraries

* argon2
* hashlib
* hmac
* math
* secrets
* string
* random
* requests
* unicodedata

---

## Project Architecture

User Input Password
↓
Password Validation
↓
Pattern & Common Password Detection
↓
Category Analysis
↓
Entropy Calculation
↓
Strength Classification
↓
Security Report Generation
↓
Breach Detection
↓
Results Display

---

## Complexity Analysis

The password validation process performs a linear scan through the password and operates in:

Time Complexity: O(n)

Where n is the password length.

This allows efficient analysis even for long passwords.

---

## Future Improvements

Potential future enhancements include:

* Multi-language support
* Password history tracking
* Dark/Light theme switching
* Offline breach database support
* Password policy customization
* Security dashboard and analytics

---

## Internship Information

Developed as part of the DecodeLabs Internship Program.

The original requirement was to implement a Password Strength Checker. Additional security analysis, breach detection, and secure password generation features were independently designed and implemented to extend the project's functionality.

---

## Author

Malik Abdullah

DecodeLabs Internship Project
