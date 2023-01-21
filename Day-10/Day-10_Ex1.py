def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


FName = input("Enter your first name: ")
LName = input("Enter your last name: ")

print(format_name(FName, LName))

