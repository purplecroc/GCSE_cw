USER_PASSWORD_FILE = "passwordfile.txt"
HIGH_SCORES_FILE = "scores.txt"

from questions import QUESTIONS

# SUBROUTINE store_login_details(username, password)​
#     file <- openWrite("passwordfile.txt")​
#     file.wrtireLine(username + ":" + password)​
#     file.close()​
# ENDSUBROUTINE
def store_login_details(username, password):
    file = open(USER_PASSWORD_FILE, "a")
    line = username + ":" + password + "\n"
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
        password = input("input password: ")
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
        (user, pwd) = line.strip().split(":")
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
        # Reset the score if we are playing again
        score = 0
        for question, answers in QUESTIONS.items():
            ask_question(question, answers)
            player_answer = None
            while player_answer == None:
                try:
                    i = int(input("Answer (1, 2, 3, 4)? "))
                    if i in range(1,5):
                        player_answer = i
                except ValueError:
                    i = None
            (_, correct) = answers[player_answer-1]
            if correct == True:
                score += 1
        print("You got", score, "correct")
        playing_quiz = play_again()
    print("Thank you for playing")
    return score

# SUBROUTINE add_score(username, score)​
#     file <- openWrite("scores.txt")​
#     file.writeLine(username + ":" + score)​
#     file.close()​
# ENDSUBROUTINE
def add_score(username, score):
    file = open(HIGH_SCORES_FILE, "a")
    line = username + ":" + str(score) + "\n"
    file.writelines(line)
    file.close()
    
# SUBROUTINE selection_sort(array)​
#     FOR i in range(LEN(array))​
#         largest_index <- i​
#         FOR j in range(i+1,LEN(array))​
#             IF array[j].score > array[largest_index].score​
#                 largest_index <- j​
#             ENDIF​
#         ENDFOR​
#         temp <- array[i]​
#         array[i] <- array[largest_index]​
#         array[largest_index] <- temp​
#     ENDFOR​
# ENDSUBROUTINE
def selection_sort(array):
    for i in range(len(array)):
        largest_index = i
        for j in range(i+1, len(array)):
            if array[j][1] > array[largest_index][1]:
                largest_index = j
        temp = array[i]
        array[i] = array[largest_index]
        array[largest_index] = temp

# SUBROUTINE sort_and_output()​​
#     file <- openRead("scores.txt")​
#     scores <- []​
#     DO ​
#         (username, score) <- file.readLine.split(":")​
#         scores[LEN(unsorted)] <- (username, score)​
#     UNTIL file.endOfFile()​
#     file.close()​
#     selection_sort(scores)​
#     FOR i in range(5)​
#         PRINT(sorted[i])​
#     ENDFOR​
# ENDSUBROUTINE       
def sort_and_output():
    file = open(HIGH_SCORES_FILE, "r")
    scores = []
    lines = file.readlines()
    for line in lines:
        (username, score) = line.strip().split(":")
        scores.append((username, score))
    file.close()
    selection_sort(scores)
    
    print("High scores:")
    max = min(5, len(scores))
    for i in range(max):
        (name, score) = scores[i]
        print(i+1, ": ", name, "scored", score)

def play_quiz():
    print("Welcome to the quiz")
    # Ask for the user to login
    username = login()
    # Play the quiz
    score = quiz()
    # Add the players score to the high score file
    add_score(username, score)
    # Output the top 5 scores
    sort_and_output()
    
play_quiz()