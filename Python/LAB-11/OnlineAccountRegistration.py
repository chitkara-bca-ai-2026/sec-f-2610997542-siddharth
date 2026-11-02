
username = input("Enter your username: ")
password = input("Enter your password: ")

length_valid = len(password) >= 8

digit_valid = False
uppercase_valid = False

for ch in password:
    if ch.isdigit():
        digit_valid = True

    if ch.isupper():
        uppercase_valid = True

print()
print("========================================")
print("PASSWORD VALIDATION REPORT")
print("========================================")

print("Username:", username)
print("Password:", "*" * len(password))

print()
print("--- Validation Rules ---")

if length_valid:
    print("[PASS] Minimum 8 characters (" + str(len(password)) + " characters)")
else:
    print("[FAIL] Minimum 8 characters")

if digit_valid:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase_valid:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print()
print("--- Result ---")

if length_valid and digit_valid and uppercase_valid:
    print("Password is VALID!")
    print("Account created successfully for " + username + "!")
else:
    print("Password is INVALID!")

print("========================================")
