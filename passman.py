import sqlite3
import os
import encryptdecrypt as ed

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
    username varchar(255) Primary Key ,
    masterpassword varchar(255))
""")

insertintoaccounts = """
insert into accounts(username, masterpassword)
values(?,?)
"""



getpassword = """
select masterpassword from accounts where username = ?
"""

pwordquery = cur.execute(getpassword, ('jshea',))
pword = pwordquery.fetchone()[0]
print(ed.check_password('password', pword))


con.commit()


