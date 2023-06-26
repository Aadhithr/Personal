Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:/Work/programming club/yourName.py ===
What is your name?/n
Hi,  
>>> 
=== RESTART: C:/Work/programming club/yourName.py ===
What is your name?
aadhith
Hi,  aadhith
>>> 
=== RESTART: C:/Work/programming club/yourName.py ===
What is your name?
Hi,  
>>> 
============ RESTART: C:/Work/programming club/yourName.py ===========
What is your name?	
Hi,  
>>> aadhith
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    aadhith
NameError: name 'aadhith' is not defined
>>> 
============ RESTART: C:/Work/programming club/yourName.py ===========
What is your name?	
Hi,  
>>> 
============ RESTART: C:/Work/programming club/yourName.py ===========
What is your name?	aadhith
Hi,  aadhith
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
write width3
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 5, in <module>
    print(length*width)
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
write width3
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 5, in <module>
    print("length"*"width")
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
write width3
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 5, in <module>
    print(length*width)
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
write width3
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 5, in <module>
    print("area = ", length * width)
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 3, in <module>
    length = int("write length")
ValueError: invalid literal for int() with base 10: 'write length'
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 4, in <module>
    width = int("write width")
ValueError: invalid literal for int() with base 10: 'write width'
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 4, in <module>
    width = intput("write width")
NameError: name 'intput' is not defined
>>> 3
3
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length2
write width3
area =  6
>>> area =  6
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=========== RESTART: C:/Work/programming club/calculator.py ==========
write length
write width
Traceback (most recent call last):
  File "C:/Work/programming club/calculator.py", line 5, in <module>
    print("area = ",int(length) *int(width))
ValueError: invalid literal for int() with base 10: ''
>>> import turtle
>>> x="aadhith"
>>> print(5*"x")
xxxxx
>>> print(5*x)
aadhithaadhithaadhithaadhithaadhith
>>> 
>>> 
>>> print(5x)
SyntaxError: invalid syntax
>>> exit
