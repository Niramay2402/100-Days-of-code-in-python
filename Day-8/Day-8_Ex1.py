# defining functions
def greet():
    print("Hello World")
    print("Hii")
    print("How's Life..?")


# greet()

# functions with inputs

def greet_with_name(name, location):
    print(f"Hello {name} ")
    print(f"What is it like in {location}?")


# greet_with_name("Neil","Vadodara")


# function with key arguments--> tells which argument is with which parameter
greet_with_name(location="surat", name="nir")
