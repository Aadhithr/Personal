#testScores.py

import turtle

students = ["Bob", "Fredd", "Barry", "Angelina", "Ayden"]
score=[ ]

print("Students")

for x in range(5):
    print(x + 1, ".", students[x])

for i in range(5):
    x = "Score of"+ students[i]
    b = int(turtle.numinput("TestScores", x, 0, 0, 20))
    score.append(b)

print("\n")

for x in range(5):
    print(x + 1, ".", students[x], "-", score[x],"/20")



    



  





    

