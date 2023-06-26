import sqlite3

#so sqlite3 is a database and lets u code in SQL(database language) to add stuff to databases

#connecting to database
def connect():
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS healthinfo (id INTEGER PRIMARY KEY, recordid text, insurance text, firstname text, lastname text, medicaldetails text)")
    conn.commit()
    conn.close()

#the insert button
#so what this does is it makes a entry in the data base after it recieves the 4 values which are located in the parameter in the function
#it recieves this through the frontend file

def insert(recordid, insurance, firstname, lastname,medicaldetails):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO healthinfo VALUES (NULL, ?, ?, ?, ?,?)", (recordid, insurance, firstname, lastname, medicaldetails))
    conn.commit()
    conn.close()

#just gets all the entries and returns the entries im pretty sure in a tuple if i remember correctly

def view():
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM healthinfo")
    rows=cur.fetchall()
    conn.close()
    return rows

#so this is the serach and SQL already has a method to search so we just get the parameters again and use the search function to get the entries with whatever filters we add

def search(recordid='', insurance='', firstname='', lastname=''):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM healthinfo WHERE recordid=? OR insurance=? OR firstname=? OR lastname=?", (recordid, insurance, firstname, lastname))
    rows=cur.fetchall()
    conn.close()
    return rows

#delete just deletes the entry 

def delete(id):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM healthinfo WHERE id=?", (id, ))
    conn.commit()
    conn.close()

#update works similar to add but instead of create it uses the update function in SQL
def update(id, recordid, insurance, firstname, lastname, medicaldetails):
    conn = sqlite3.connect("healthrec.db")
    cur = conn.cursor()
    cur.execute("UPDATE healthinfo SET recordid=?, insurance=?, firstname=?, lastname=?, medicaldetails=? WHERE id=?", (recordid, insurance, firstname, lastname, medicaldetails, id))
    conn.commit()
    conn.close()


connect()
