# Dictionary using database

#import python sql connector 
import mysql.connector

#connecting to [udemy Ardit Sulce's] database
mydb = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = mydb.cursor()



#function to give the def of the word
def definition():
    word = input("Enter a word to get its definition: ")
    # loop to handle word suggestion case
    while(True):
        # query the database for the given word
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
        result1 = cursor.fetchall()
        # checks if the result is empty or not
        if result1:
            # prints the meaning 
            for meaning in result1:
                print(meaning[1])
        else:
            # given word doesn't exist so suggests similar word
            query2 = cursor.execute("SELECT * FROM Dictionary WHERE SOUNDEX(Expression) LIKE SOUNDEX('{}')".format(word))
            result2 = cursor.fetchall()
            y_n = input("Did you mean {}? [Y/N]: ".format(result2[0][0]))
            if y_n == "Y":
                word = result2[0][0]
                # got the right word and does the work again in the while loop
                continue
            else:
                print("No word found!!")
        # we are done so lets break the loop
        break
        
        
        
definition()
    
    