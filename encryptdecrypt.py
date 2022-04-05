from tabnanny import check
from cryptography.fernet import Fernet
import bcrypt

class password_and_salt():
    def __init__(self, passwordandsalt):
        self.hashpassword = passwordandsalt[29:]
        self.salt = passwordandsalt[:29]
    

def get_hashed_password_and_salt(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_text_password, salt) 


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


p = password_and_salt(get_hashed_password_and_salt('password'))

print(p.hashpassword)
print(p.salt)

print(check_password('password', p.salt+p.hashpassword))