# Password Generator (CLI)

This is a Python command-line password generator.
It creates secure random passwords based on user preferences.

## Features
- User-defined password length
- Minimum length validation
- Option to include:
  - Letters (A–Z, a–z)
  - Numbers (0–9)
  - Symbols (!@#$...)
- Input validation (prevents crashes)
- Random password generation

## Concepts Used
- random module
- string module
- while loop
- for loop
- input validation
- try / except (exception handling)
- string concatenation
- f-strings

## How It Works
1. User enters desired password length.
2. Program validates the input.
3. User selects character types (letters, numbers, symbols).
4. Program builds a character pool.
5. Random characters are selected to generate the password.

## How to Run
1. Open terminal in this folder.
2. Run:

   python main.py

## Example

Enter password length (minimum 4): 10  
Include letters? (y/n): y  
Include numbers? (y/n): y  
Include symbols? (y/n): n  

Generated Password: A7kLp2xQ9m

## Notes
- At least one character type must be selected.
- Password is generated randomly each time.
- The program handles invalid inputs safely.