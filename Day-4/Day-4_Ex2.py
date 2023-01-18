import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names)

y = random.randint(0, x-1)

print(f"{names[y]} is going to buy the meal today!")
