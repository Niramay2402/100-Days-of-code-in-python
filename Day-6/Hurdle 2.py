#import random 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
#numberOfHurdles = random.randint(1,6)
numberOfHurdles = 0
#print(numberOfHurdles)

while not at_goal():
    jump()
    #numberOfHurdles -= 1


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
