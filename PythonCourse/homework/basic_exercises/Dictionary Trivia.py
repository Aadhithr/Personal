import random
import turtle
easy = {}
medium = {}
hard = {}
temp_dict = {}
temp_list = []
choices = []
Admin_User = "dshf"
while Admin_User != "exit":
    Admin_User = input("Do you want to [Create] or [Answer] questions or [Exit]? ")
    if Admin_User == "create":
       NoOfQns = int(input("How many questions do you want to make?"))
       QLevel = input("What is the level of complexity(Easy, Medium, Hard)")
       if QLevel == "easy": 
            for QnNo in range(NoOfQns):
                Qn = input("Enter Question:")
                for i in range(4):
                    temp_string = "Enter choice # ", i+1
                    Choice = input(temp_string)
                    temp_list.append(Choice)
                CrtAns = input("Enter the correct answer:")
                temp_list.append(CrtAns)
                temp_dict[Qn] = temp_list
                temp_list = []
                easy[QnNo + 1] = temp_dict
                temp_dict = {}
       if QLevel == "medium":
             for QnNo in range(NoOfQns):
                Qn = input("Enter Question:")
                for i in range(4):
                    temp_string = "Enter choice # ", i+1
                    Choice = input(temp_string)
                    temp_list.append(Choice)
                CrtAns = input("Enter the correct answer:")
                temp_list.append(CrtAns)
                temp_dict[Qn] = temp_list
                temp_list = []
                medium[QnNo + 1] = temp_dict
                temp_dict = {}
       if QLevel == "hard":
             for QnNo in range(NoOfQns):
                Qn = input("Enter Question:")
                for i in range(4):
                    temp_string = "Enter choice # ", i+1
                    Choice = input(temp_string)
                    temp_list.append(Choice)
                CrtAns = input("Enter the correct answer:")
                temp_list.append(CrtAns)
                temp_dict[Qn] = temp_list
                temp_list = []
                hard[QnNo + 1] = temp_dict
                temp_dict = {}
    if Admin_User == "answer":
           print(medium)
           #NoOfQns = turtle.numinput("Trivia", "How many questions do you want to answer?",1, 0, len(easy))
           NoOfQns = int(input("How many questions do you want to answer?"))
           QLevel = input("What is the level of complexity(Easy, Medium, Hard)")
           if QLevel == "easy":
               for i in range(int(NoOfQns)):
                    Qn_No = random.randint(1, NoOfQns)
                    temp_dict = easy.get(Qn_No)
                    Qn = list(temp_dict.keys())
                    choices = list(temp_dict.values()).pop()
                    print("Qn #",i+1,". ",Qn[0])
                    print("Your choices are:")
                    for j in range(4):
                        print(choices[j])
                    ans = input("Enter the right answer")
                   
                    if ans == choices[-1]:
                        print("Correct :)")
                    else:
                        print("Incorrect :(")

           if QLevel == "medium":
               for i in range(int(NoOfQns)):
                    Qn_No = random.randint(1, NoOfQns)
                    temp_dict = medium.get(Qn_No)
                    Qn = list(temp_dict.keys())
                    choices = list(temp_dict.values()).pop()
                    print("Qn #",i+1,". ",Qn[0])
                    print("Your choices are:")
                    for j in range(4):
                        print(choices[j])
                    ans = input("Enter the right answer")
                   
                    if ans == choices[-1]:
                        print("Correct :)")
                    else:
                        print("Incorrect :(")

           if QLevel == "hard":
               for i in range(int(NoOfQns)):
                    Qn_No = random.randint(1, NoOfQns)
                    temp_dict = hard.get(Qn_No)
                    Qn = list(temp_dict.keys())
                    choices = list(temp_dict.values()).pop()
                    print("Qn #",i+1,". ",Qn[0])
                    print("Your choices are:")
                    for j in range(4):
                        print(choices[j])
                    ans = input("Enter the right answer")
                   
                    if ans == choices[-1]:
                        print("Correct :)")
                    else:
                        print("Incorrect :(")
          
          
          
                    
                    
                          

        

           
   

   

    
   
        

