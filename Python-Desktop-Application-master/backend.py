import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book values(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title=? OR author=? or year=? or isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(year,author):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book set year=? where author=?",(year,author))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=?",(id,))
    conn.commit()
    conn.close()

connect()
#insert("Agni Siragugal","APJ Abdul Kalam",1985,10101)
#insert("Karuvaachi Kaaviyam","Vairamuthu",1988,10105)
#insert("En iniya iyandhira","Sujatha",1999,10109)
#insert("Malgudi Days","RK Narayan",1975,10115)

#print(search(year="1975"))
#update(1979,"APJ Abdul Kalam")
#delete(3)
print(view())
