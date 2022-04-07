import os
import encryptdecrypt as ed
import SQL
import basicfunctions as bf
# dir_path = os.path.dirname(os.path.realpath(__file__))
SQL.initialize_main_database()    

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



# SQL.create_new_account('jshea','password')

