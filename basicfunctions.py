import encryptdecrypt as ed
import SQL

def set_hashed_password(pwd):
    return (ed.get_hashed_password_and_salt(pwd))

def set_user_name(username):
    return username

def check_password(password, username):
    return ed.check_password(password, SQL.get_password(username))

