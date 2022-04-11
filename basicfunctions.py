import encryptdecrypt as ed
import SQL

class currentUser():
    def __init__(self, username, decryptkey) -> None:
        
        self.loggedin = True
        self.username = username
        self.decryptkey = decryptkey
    def logout(self):
        self.loggedin = False
        self.username = 'No User Logged in'
        self.decryptkey = ''
        


#----Account Functions---------


def add_user(username, password):
    password = set_hashed_password(password)
    SQL.create_new_account(username, password)

def set_hashed_password(pwd):
    return (ed.get_hashed_password_and_salt(pwd))

def check_password(password, username):
    return ed.check_password(password, SQL.get_password(username))

def login(username, password):
    if check_password(password, username):
        
        salt = SQL.get_password(username)[:29]
        dk = ed.generate_decrypt_key(password, salt)     
        currentuser = currentUser(username, dk)
        return currentuser

    else:
        currentuser = currentUser('', '')
        currentuser.logout()
        return currentuser



#------SQL Functions-----------

def add_passwords(site, siteusername, password, username, key):
    password = ed.encrypt_userpasswords_password(password, key)
    SQL.insert_item_userpasswords(site, siteusername,  password, username)

def get_encrypted_password(idx, key):
    encryptedpw = SQL.get_userPasswords_password(idx)
    return ed.decrypt_userpassword_password(encryptedpw, key)
def delete_password(pwdidx):
    SQL.delete_password(pwdidx)

