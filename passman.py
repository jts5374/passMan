import os
import encryptdecrypt as ed
import SQL
import basicfunctions as bf
# dir_path = os.path.dirname(os.path.realpath(__file__))
SQL.initialize_main_databases()    

# activeuser = bf.login('jshea', 'password')

# print(activeuser.username)
# print(activeuser.decryptkey)

# print(bf.get_all_userpasswords(activeuser.username))


print(SQL.user_exists('jj'))
#bf.add_passwords('amazon', 'test@msn.com', 'fjdksla;fjkdjfaksdjfdklsajfdksjafkdsjfkalsjdfkldsjalfkjdslafjdsklfjal', activeuser.username, activeuser.decryptkey)
# activeuser.logout()
# print(bf.get_encrypted_password(4, activeuser.decryptkey))


# print(activeuser.username)
# print(activeuser.decryptkey)

