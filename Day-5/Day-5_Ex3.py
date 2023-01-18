#get the  sum of even numbers

total = int(input("Enter any number: "))

total_even = 0

for number in range(1,total):
    if (number%2) == 0:
        total_even += number

print(total_even)