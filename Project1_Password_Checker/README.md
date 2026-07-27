# Project 1: Password Strength Checker 

**DecodeLabs Cyber Security Internship **

## Overview

A Python command-line tool that evaluates a password and classifies it as
**Weak**, **Medium**, or **Strong** based on length and character variety.
This project focuses on core security logic, data validation, string
handling, and conditional checks , rather than any actual "hacking."

Weak or reused passwords are behind a huge share of real-world breaches
(Verizon's DBIR reports 81% of hacking-related breaches involve weak or
stolen passwords), so this kind of validation is a genuinely useful first
line of defense before any hashing or encryption happens.

## Features

- **Length check** — passwords under 8 characters automatically fail
- **Character variety checks** — detects uppercase, lowercase, digits, and symbols
- **Scoring system** — 1 point per variety check passed, plus a bonus point for length ≥ 12
- **Strength classification** — Weak / Medium / Strong based on total score
- **Common leaked password check (bonus)** — rejects passwords found in a small sample list of frequently leaked passwords (e.g. `123456`, `password`, `qwerty`)

> Note: the leaked-password list here is a small hardcoded sample for
> demonstration purposes. A production system would check against a real
> breach database (e.g. Have I Been Pwned's API) instead.

## How to Run

```bash
python password_strength_checker.py
```

Then enter a password when prompted. Type `quit` to exit.

### Example output

```
=== Password Strength Checker ===

Enter a password to check (or 'quit' to exit): MyStr0ng!Pass2026

Password: ****************  (length: 17)
----------------------------------------
Length >= 8 chars      : True
Contains uppercase     : True
Contains lowercase     : True
Contains digit         : True
Contains symbol        : True
Score                  : 5
Strength               : Strong
----------------------------------------
```

## Key Skills Practiced

- String handling and iteration
- Conditional logic and short-circuit evaluation (`any()`)
- Function design with type hints and default parameters
- Basic security awareness: entropy, common password lists, and why
  validating input before any hashing/encryption step matters

## Tech Used

- Python 3 (standard library only — `string` module)
