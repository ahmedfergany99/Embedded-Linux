import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

if 1 <= month <= 12:
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:\n")
    print(cal)
else:
    print("Invalid month. Please enter a month between 1 and 12.")