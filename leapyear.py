def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

year = int(input("Enter a year: "))
if is_leap(year):
 print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")