import mysql.connector
with open('passwords.txt') as passfile:
    passwords = passfile.readlines()
for password in passwords:
    try:
        print('trying password: ' , password)
        database = mysql.connector.connect(user = 'root', passwd = password.strip('\n') , host = 'localhost')
        if database.is_connected():
            print('password is:' , password)
            break
        
    except:
        pass
else: 
    print('Password not found in the list!')
