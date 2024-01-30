USER_PASSWORD_FILE = "passwordfile.txt"

QUESTIONS = {
    "Question 1": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    "Question 2": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    "Question 3": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 4": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 5": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 6": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 7": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 8": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 9": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
    # "Question 10": [("Answer 1.1", True), ("Answer 1.2", False), ("Answer 1.3", False), ("Answer 1.4", False)],
}

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
    username = input("input username: ")
    while True:
        password = input("input password: ") ## TEST THIS LATER
        if len(password) >= 8:
            break
        print("password must be more than 8 characters")
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
        return username
    elif command == "EXISTING":
        while True:
            (username, password) = get_user_and_password()
            if validate_user(username, password):
                return username
            else:
                print("invalid username or password")

# SUBROUTINE ask_question(question, answers)​
#  PRINT(question)​
#  FOR answer in answers​
#   PRINT(answer)​
#  ENDFOR​
# ENDSUBROUTINE

def ask_question(question, answers):
    print("Q:",question)
    for index, (answer, correct) in enumerate(answers):
        print("A " + str(index + 1) + ":", answer)
    
        

# SUBROUTINE play_again()​
#  WHILE TRUE​
#   PRINT("play again (y/n)?")​
#   IF USERINPUT = "y"​
#    RETURN TRUE​
#   ELSEIF USERINPUT = "n"​
#    RETURN FALSE​
#   PRINT("Invalid input")​
#  ENDWHILE​
# ENDSUBROUTINE

def play_again():
    while True:
        response = input("play again (y/n)? ").upper()
        if response == "Y":
            return True
        elif response == "N":
            return False
        print("invalid input")

# SUBROUTINE quiz()​
#  questions -> dictionary of questions to list of answers​
#  playing_quiz = TRUE​
#  WHILE playing_quiz​
#   FOR question and answers in questions ​
#    ask_question(question, answers)​
#   ENDFOR​
#   playing_quiz = play_again()​
#  ENDWHILE​
#  PRINT("Thank you for playing")
# ENDSUBROUTINE

def quiz():
    playing_quiz = True
    score = 0
    while playing_quiz:
        for question, answers in QUESTIONS.items():
            ask_question(question, answers)
            player_answer = None
            while player_answer == None:
                try:
                    i = int(input("answer (1, 2, 3, 4)? "))
                    if i in range(1,5):
                        player_answer = i
                except ValueError:
                    i = None
            (_, correct) = answers[player_answer-1]
            if correct == True:
                score += 1
        print("you got", score, "correct")
        playing_quiz = play_again()
    print("thank you for playing")
    return score

# SUBROUTINE add_score(username, score)​
#     file <- openWrite("scores.txt")​
#     file.writeLine(username + ":" + score)​
#     file.close()​
# ENDSUBROUTINE

def add_score(username, score):
    file = open("scores.txt", "a")
    line = username + ":" + score
    file.writelines(line)
    file.close()

# ask_question("blah?", ["b;ah", "bleh", "bloo"])

# username = None
# while username == None:
#     username = login()
# print(username)

def play_quiz():
    username = login()
    score = quiz()
    

quiz()