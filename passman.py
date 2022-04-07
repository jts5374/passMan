import os
import encryptdecrypt as ed
import SQL

class User():
    def __init__(self, username, mainpassword):
        self.username = username
        self.mainpassword = mainpassword
        self.accounts = []

dir_path = os.path.dirname(os.path.realpath(__file__))
SQL.initialize_main_database(os.path.join(dir_path, 'passMan.db'))    

# con = sqlite3.connect(os.path.join(dir_path, 'passMan.db'))
# cur = con.cursor()
# cur.execute("""
# create table if not exists accounts(   
#     username varchar(255) Primary Key ,
#     masterpassword varchar(255))
# """)


# pwordquery = cur.execute(getpassword, ('jshea',))
# pword = pwordquery.fetchone()[0]
# print(ed.check_password('password', pword))





