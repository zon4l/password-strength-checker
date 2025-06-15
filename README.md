# Password Strength Checker (CLI)

## Problem Statement
Weak or common passwords are one of the leading causes of account breaches and unauthorized access. This CLI-based tool evaluates the strength of user-provided passwords against multiple criteria to assess their resistance to brute-force, dictionary, and pattern-based attacks.

## Working / Algorithm
The script accepts a password input and calculates its strength based on a scoring system. It uses both additive and subtractive metrics to evaluate password quality:

### Additive Checks
- **Length**: Longer passwords contribute positively.
- **Character Variety**: Uppercase, lowercase, numeric, and special characters each improve strength.
- **Requirements Met**: Rewards passwords that meet minimum security standards (e.g. length and character type diversity).

### Subtractive Checks
- **Letters-only or numbers-only passwords**: Penalized due to predictability.
- **Consecutive character types**: Sequences of same-case letters or digits are penalized.
- **Sequential characters**: Penalized for patterns like "abc" or "123".
- **Common passwords**: Compared against a dictionary of weak passwords and heavily penalized.

If the password is found in the common-passwords list, a warning is displayed and a major strength penalty is applied.

### References
- **Common Password List**: Sourced from [Lucidar’s most common passwords dataset](https://lucidar.me/en/security/load-most-common-passwords-in-python/)
- **Password Strength Calculation Model**: Based on the methodology used by [PasswordMeter.com](https://passwordmeter.com/)

## Libraries Used
- `string` – Used for identifying punctuation and character classification.
- `open()` – For reading from a list of common passwords.
- Python built-in functions and data types were used extensively for logic and validation.
