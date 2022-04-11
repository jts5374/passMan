import os
import encryptdecrypt as ed
import SQL
import basicfunctions as bf
# dir_path = os.path.dirname(os.path.realpath(__file__))
SQL.initialize_main_databases()    

activeuser = bf.login('test', 'password')

print(activeuser.username)
print(activeuser.decryptkey)




#bf.add_passwords('amazon', 'test@msn.com', 'fjdksla;fjkdjfaksdjfdklsajfdksjafkdsjfkalsjdfkldsjalfkjdslafjdsklfjal', activeuser.username, activeuser.decryptkey)
# activeuser.logout()
print(bf.get_encrypted_password(4, activeuser.decryptkey))


# print(activeuser.username)
# print(activeuser.decryptkey)

