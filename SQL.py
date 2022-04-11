from doctest import master
from getpass import getpass
import sqlite3
import os
import encryptdecrypt as ed

dir_path = os.path.dirname(os.path.realpath(__file__))
con = sqlite3.connect(os.path.join(dir_path, 'passMan.db'))
cur = con.cursor()


def initialize_main_databases():
    cur.execute("""
    create table if not exists accounts(   
        UserName varchar(255) Primary Key ,
        MasterPassword varchar(255))
    """)

    cur.execute("""
    create table if not exists userpasswords(   
        AccountEntry integer Primary Key,
        Site varchar(255),
        SiteUserName varchar(255),
        Password varchar(255),
        MasterUserName varchar(255),
        Foreign Key (MasterUserName) References accounts(UserName)
        )
    """)
    
    con.commit()

#ADD New top level account
def create_new_account(username, password):
    insertintoaccounts = """
    insert into accounts(username, masterpassword)
    values(?,?)
    """
    cur.execute(insertintoaccounts, (username, password))
    con.commit()

#Add new password to userpasswords db
def insert_item_userpasswords(site, siteusername, password, masterusername):
    insertintouserpassword = """
    insert into userpasswords(Site,SiteUserName, Password, MasterUserName)
    values(?,?,?,?)
    """
    cur.execute(insertintouserpassword, (site, siteusername, password, masterusername))
    con.commit()


#update password in userpasswords db
def update_user_passwords(accountidx, password):
    alteruserpasswords = """
    Update userpasswords 
    SET Password = ?
    Where AccountEntry = ?
    """
    cur.execute(alteruserpasswords, (password, accountidx))
    con.commit()

#retrieve password from userpasswords db
def get_password(username):

    getpassword = """
    select masterpassword from accounts where username = ?
    """
    query = cur.execute(getpassword, (username,))
    return query.fetchone()[0]

def get_userPasswords_password(idx):
    getpassword= """
    select Password from userpasswords
    where AccountEntry = ?
    """
    query = cur.execute(getpassword, (idx,))
    return query.fetchone()[0]

def delete_password(idx):
    deletePassword = """
    Delete from userpasswords
    where accountentry = ? 
    """
    cur.execute(deletePassword, (idx,))
    con.commit()

def get_all_userpasswords(username):
    getall = """
    Select * from userpasswords
    where MasterUserName = ?"""
    query = cur.execute(getall, (username,))
    return query.fetchall()

def user_exists(username):
    userexists = """
    Select Exists(
        Select * from accounts
        Where username = ?)
    """
    query = cur.execute(userexists, (username,))
    return query.fetchone()[0]


