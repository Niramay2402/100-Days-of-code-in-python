#Average student heights
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#heights 150 165 132 145 168 172 120 156 143 120 

numberOfStudents = 0
total_height = 0

for x in student_heights:
    total_height = total_height + x
    numberOfStudents = numberOfStudents+1

#print(f"Number Of Students: {numberOfStudents}")
#print(f"Total height of students:{total_height}")

Average_Height = round((total_height/numberOfStudents))
print(Average_Height)