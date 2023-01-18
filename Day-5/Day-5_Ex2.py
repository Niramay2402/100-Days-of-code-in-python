#get average student scores
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# 78 52 69 41 36 98 62 34 

highest_score = 0
for score in student_scores:
    if score  > highest_score:
        highest_score = score


print(f"The highest score in the class is: {highest_score}")