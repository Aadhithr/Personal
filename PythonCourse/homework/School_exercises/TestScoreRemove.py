#testScores.py

import turtle
s = 21

students = ["Bob", "Fredd", "Barry", "Angelina", "Ayden"]
score=[ ]

print("Students")

for x in range(len(students)):
    print(x + 1, ".", students[x])

for i in range(len(students)):
    x = "Score of"+ students[i]
    b = int(turtle.numinput("TestScores", x, 0, 0, 20))
    score.append(b)

print("\n")

for x in range(len(students)):
    print(x + 1, ".", students[x], "-", score[x],"/20", "\n")
    if (s > score[x]):
        s = score[x]
m = score.index(s)
students.pop(m)
score.pop(m)

print("List after removed lowest scorer\n")
for x in range(len(students)):
    print(x + 1, ".", students[x], "-", score[x],"/20")




        
        
    





    



  





    

