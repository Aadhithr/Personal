
a = float(input("Enter the triangle's angle: "))
b = float(input("Enter the triangle's 2nd angle: "))
c = 180 - (a+b)

if a == 90 or b == 90 or c == 90:
    print("This is a right triangle")

if a < 90 and b < 90 and c < 90:
    print("This is a acute triangle")

if a > 90 or b > 90 or c > 90:
    print("This is a obtuse triangle")

d = float(input("Enter the triangle's side length: "))
e = float(input("Enter the triangle's 2nd side length: "))
f = float(input("Enter the triangle's 3rd side length: "))

if(d + e < f and e + f < d and d + f < e):
    print("This is not a triangle")

if d == e or d == f or e ==f and a == b or b == c or a ==c:
    print("This is an iscoceles triangle ")

if d == e and d ==f and e ==f and a == b and b == c and a ==c:
    print("This is an equilateral triangle ")

if d != e and d !=f and e !=f and a != b and b != c and a !=c:
    print("This is an scalene triangle")



        
