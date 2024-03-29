import encryptdecrypt as ed
import SQL

class currentUser():
    def __init__(self) -> None:
        self.username= ''
        self.decryptkey=''
        
    def login(self, username, password):   
        self.loggedin = True
        self.username = username
        salt = SQL.get_password(username)[:29]
        dk = ed.generate_decrypt_key(password, salt) 
        self.decryptkey = dk
    def logout(self):
        self.loggedin = False
        self.username = 'No User Logged in'
        self.decryptkey = ''
        


#----Account Functions---------

def startup():
    SQL.initialize_main_databases()

def add_user(username, password):
    password = set_hashed_password(password)
    SQL.create_new_account(username, password)

def remove_ups_account(idx):
    SQL.delete_password(idx)
    
def set_hashed_password(pwd):
    return (ed.get_hashed_password_and_salt(pwd))

def check_password(password, username):
    return ed.check_password(password, SQL.get_password(username))

def login(username, password):
   
    if check_password(password, username):
        
        currentuser = currentUser()    
        currentuser.login(username, password)
        return currentuser

    else:
        currentuser = currentUser()
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

def get_all_userpasswords(username):
    return SQL.get_all_userpasswords(username)

def userexists(username):
    return SQL.user_exists(username)

