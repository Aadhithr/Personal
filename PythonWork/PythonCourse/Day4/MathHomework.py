print("MathHomework.py")

#Ask the user to enter a math problem
problem = input("Enter a math problem, or 'q' to quit: ")

#Keep going until the user enters 'q' to quit
while (problem != "q"):
    
     # Show the problem, and the answer using eval()
    print("The answer to ", problem, "is:", eval(problem) )
    
     # Ask the user for another problem
    problem = input("Enter another math problem, or 'q' to quit:")

#out of loop
print("I'm done with my math homework")
