
print("========================================")
print("      CALENDAR VERIFICATION SYSTEM")
print("========================================")

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Year must be a positive integer.")

else:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "LEAP YEAR"
            reason = "Century year divisible by 400"
        else:
            status = "COMMON YEAR"
            reason = "Century year not divisible by 400"

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"

    if status == "LEAP YEAR":
        days = 366
        february_days = 29
    else:
        days = 365
        february_days = 28

    print()
    print("----------------------------------------")
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", days, "days")
    print("Days in February:", february_days, "days")
    print("Reason:", reason)
    print("----------------------------------------")
