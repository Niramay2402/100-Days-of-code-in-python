#to generate same sequence of variables
import random
 
random.seed(1)
 
# Get the state of the generator
state = random.getstate()
 
print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
 
# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))