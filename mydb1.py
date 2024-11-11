import sqlite3

class Database:
    def __init__(self,db) :
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''create table if not exists users
                         (id integer primary key,
                         fname text,
                         lname text,
                         email text,
                         password text )''')
        self.con.commit()
    
    def insert(self,fname,lname,email,password):
        self.cur.execute(''' insert into users values (null,?,?,?,?)''',
                         (fname,lname,email,password))
        
        self.con.commit()
    
    def search(self,email,password):
        self.cur.execute("select * from users where email =? and password =? ",(email,password))
        record = self.cur.fetchall()
        return record
    