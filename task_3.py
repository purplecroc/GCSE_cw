USER_PASSWORD_FILE = "passwordfile.txt"

# SUBROUTINE store_login_details(username, password)​
#     file <- openWrite("passwordfile.txt")​
#     file.wrtireLine(username + ":" + password)​
#     file.close()​
# ENDSUBROUTINE

def store_login_details(username, password):
    file = open(USER_PASSWORD_FILE, "a")
    line = username + ":" + password
    file.writelines(line)
    file.close()

# SUBROUTINE get_user_and_password()​
#     PRINT("input username")​
#     username <- USERINPUT​
#     PRINT("input password")​
#     password <- USERINPUT​
#     RETURN (username, password)​
# ENDSUBROUTINE

def get_user_and_password():
    username = input("input username ")
    password = input("input password ")
    return (username, password)

# SUBROUTINE validate_user(username, password)​
#     file <- openRead("passwordfile.txt")​
#     DO ​
#         (user, pass) = file.readLine.split(":")​
#         IF user = username AND pass = password​
#             file.close()​
#             RETURN True​
#         ENDIF​
#     UNTIL file.endOfFile()​
#     file.close()​
#     RETURN False​
# ENDSUBROUTINE

def validate_user(username, password):
    file = open(USER_PASSWORD_FILE, "r")
    ret = None
    lines = file.readlines()
    for line in lines:
        (user, pwd) = line.split(":")
        if user == username and pwd == password:
            file.close()
            return True
    file.close()
    return False  

# SUBROUTINE login()​
#     PRINT("new or existing user")​
#     command <- USERINPUT.UPPER()​
#     IF command = "NEW"​
#         (username, password) = get_user_and_password()​
#         store_login_details(username, password)​
#     ELSEIF command = "EXISTING"​
#         WHILE True​
#             (username, password) = get_user_and_password()​
#             IF validate_user(username, password)​
#                 RETURN username ​
# ENDSUBROUTINE   

def login():
    command = input("new or existing user? ").upper()
    if command == "NEW":
        (username, password) = get_user_and_password()
        store_login_details(username, password)
    elif command == "EXISTING":
        while True:
            (username, password) = get_user_and_password()
            if validate_user(username, password):
                return username
            else:
                print("invalid username or password")

username = None
while username == None:
    username = login()
print(username)