from hashlib import pbkdf2_hmac
from cryptography.fernet import Fernet
import bcrypt
import base64
import os
from pbkdf2 import PBKDF2
import pbkdf2
import pyDes

class password_and_salt():
    def __init__(self, plain_text_password):
        password_and_salt = get_hashed_password_and_salt(plain_text_password)
        self.hashpassword = password_and_salt[29:]
        self.salt = password_and_salt[:29]
    

def get_hashed_password_and_salt(plain_text_password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_text_password, salt) 


def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

def generate_decrypt_key(plain_text_password, salt):
    return PBKDF2(plain_text_password, salt).read(16)

def encrypt_userpasswords_password(plain_text_password, key):
    return pyDes.triple_des(key).encrypt(plain_text_password, padmode=2)

def decrypt_userpassword_password(encryptedpassword, key):
    return pyDes.triple_des(key).decrypt(encryptedpassword, padmode = 2).decode()


p = password_and_salt('password')

# print(p.hashpassword)
# print(p.salt)

# print(check_password('password', p.salt+p.hashpassword))





