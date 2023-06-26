import sqlite3

#so sqlite3 is a database and lets u code in SQL(database language) to add stuff to databases

#connecting to database
def connect():
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

#the insert button
#so what this does is it makes a entry in the data base after it recieves the 4 values which are located in the parameter in the function
#it recieves this through the frontend file

def insert(title, author, year, isbn):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

#just gets all the entries and returns the entries im pretty sure in a tuple if i remember correctly

def view():
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

#so this is the serach and SQL already has a method to search so we just get the parameters again and use the search function to get the entries with whatever filters we add

def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

#delete just deletes the entry 

def delete(id):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id, ))
    conn.commit()
    conn.close()

#update works similar to add but instead of create it uses the update function in SQL
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
