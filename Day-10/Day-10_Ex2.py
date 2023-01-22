# Days in month and adding 1 day in Feb for leap year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):

    if month < 1 or month > 12:
        return "Invalid month entered"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        month_days[1] = 29
        days = month_days[month - 1]
    else:
        days = month_days[month - 1]

    return f"{days}"


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







