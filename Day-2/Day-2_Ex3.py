# LIFE/TIME LEFT TO LIVE
age = int(input("What is your current age? "))

# in 90 yrs how many days, weeks and months are there
days_in_90yrs = 90*365
weeks_in_90yrs = 90*52
months_in_90yrs = 90*12

# to count your current age how many days, weeks and months u have lived
days_lived = age*(365)
weeks_lived = age*(52)
months_lived = age*12

days_left = days_in_90yrs - days_lived
weeks_left = weeks_in_90yrs - weeks_lived
months_left = months_in_90yrs - months_lived

#print(days_lived,days_left,days_in_90yrs)
#print(weeks_lived,weeks_left,weeks_in_90yrs)
#print(months_lived,months_left,months_in_90yrs)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")