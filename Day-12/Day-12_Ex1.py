enemies = 1


# enemies is not have global scope// isnt a global variable
# def increase_enemies():
#     enemies +=1
#     print(enemies)


# def increase_enemies():
#     enemies = 0
#     print(f"enemies inside {enemies+1}")
#     return f"{enemies+1}"

def increase_enemies():
    global enemies  # here global makes the scope of the variable global
    enemies += 1
    print(enemies)


increase_enemies()

PI = 3.1428  # knowing Scope can be while defining Global constants

#
# def a_function(a_parameter):
#     global a_variable
#     a_variable = 15
#     return a_parameter
#
#
# a_function(10)
# print(a_variable)