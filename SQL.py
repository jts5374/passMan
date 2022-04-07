import sqlite3
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
con = sqlite3.connect(os.path.join(dir_path, 'passMan.db'))
cur = con.cursor()


def initialize_main_database(path):
    cur.execute("""
    create table if not exists accounts(   
        username varchar(255) Primary Key ,
        masterpassword varchar(255))
    """)
    con.commit()

def create_new_account():
    insertintoaccounts = """
    insert into accounts(username, masterpassword)
    values(?,?)
    """




getpassword = """
select masterpassword from accounts where username = ?
"""
