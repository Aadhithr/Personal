import mysql.connector

mydb = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = mydb.cursor()




def definition():
    word = input("Enter a word to get its definition: ")
    while(True):
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
        result1 = cursor.fetchall()
    
        if result1:
            for meaning in result1:
                print(meaning[1])
        else:
            query2 = cursor.execute("SELECT * FROM Dictionary WHERE SOUNDEX(Expression) LIKE SOUNDEX('{}')".format(word))
            result2 = cursor.fetchall()
            y_n = input("Did you mean {}? [Y/N]: ".format(result2[0][0]))
            if y_n == "Y":
                word = result2[0][0]
                continue
            else:
                print("No word found!!")
        break
        
        
        
definition()
    
    