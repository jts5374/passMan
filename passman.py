import sqlite3
import os

class User():
    def __init__(self, username, mainpassword):
        self.username = username
        self.mainpassword = mainpassword
        self.accounts = []
    
dir_path = os.path.dirname(os.path.realpath(__file__))
con = sqlite3.connect(os.path.join(dir_path, 'passMan.db'))
cur = con.cursor()
cur.execute("""
create table if not exists accounts(
    userid integer Primary Key,   
    username varchar(255) ,
    masterpassword varchar(255))
""")

cur.execute("""
insert into accounts(username, password)
values('test', 'testing')
""")

con.commit()