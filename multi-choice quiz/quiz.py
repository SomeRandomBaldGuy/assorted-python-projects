#This acts as a basic quiz game in python.
#The questions are various programming and operating system related topics.

import time

#------------------

def quiz():
     guesses = []
     correct_guesses = 0
     question_num = 1
     for key in questions:
          print ("------------------")
          print (key)
          for i in options [question_num-1]:
               print (i)
          guess = input ("Enter your choice: (A, B, C, D): ")
          guess = guess.upper()
          guesses.append(guess)
          correct_guesses += check_answers(questions.get(key), guess) 
          question_num += 1
     score(correct_guesses, guesses)
     
#------------------

def check_answers(answer, guess):
     if answer == guess:
          time.sleep(1)
          print ("Correct!")
          return 1
     else:
          time.sleep(1)
          print ("Incorrect!")
          return 0

#------------------

def score(correct_guesses, guesses):
     print ("------------------")
     print ("Your Results")
     print ("------------------")
     
     print ("Answers: ", end="")
     for i in questions:
          print (questions.get(i), end=" ")
     print()
     
     print ("Guesses: ", end="")
     for i in guesses:
          print (i, end=" ")
     print()
     
     score = int((correct_guesses/len(questions))*100)
     print ("Your total score is: "+ str(score) +"%.")

#------------------

def play_again():
     response = input ("Would you like to play again? (Yes or No): ")
     response = response.lower()
     
     if response == "yes":
          return True
     elif response == "no":
          return False
     else:
          print ("You must choose yes or no.")
          play_again()

#------------------

#Key-Value pairs for checking against user supplied answers.
questions = {
     "Who designed the 'C' programming language?: ": "B",
     "Who originally wrote the Linux Kernel?: ": "C",
     "Which of the following is a popular enterprise version of GNU/Linux?: ": "A",
     "When was the first offical realease of the Linux Kernel?: ": "D",
     "Who is the mascot of the Linux Kernel?: ": "B",
     "What service typically uses the networking port '22'?: ": "A",
     "Which of the following is a commonly used Web Server application?: ": "D"
}

#2D List of the possible answers for the given questions.
options = [["A. Steve Wozniak", "B. Dennis Ritchie", "C. Richard Stallman", "D. Bill Gates"],
          ["A. Ken Thompson", "B. Steve Jobs", "C. Linus Torvalds", "D. Brian Kernighan"],
          ["A. Red Hat Enterprise Linux", "B. Ubuntu Linux", "C. Arch Linux", "D. Slackware Linux"],
          ["A. 1983", "B. 1975", "C. 1998", "D. 1991"],
          ["A. Spot", "B. Tux", "C. Rufus", "D. Buddy"],
          ["A. SSH", "B. FTP", "C. HTTPS", "D. DNS"],
          ["A. FileZilla", "B. Thunderbird", "C. VLC", "D. Apache"]]

quiz()

while play_again():
     quiz()
          
###################################################################################################
#                                                                                                 #
#     _  __             _          _   _             _      _  _             _                    #
#    | |/ / ___ __   __(_) _ __   | | | | _   _   __| |  __| || |  ___  ___ | |_  ___   _ __      #
#    | ' / / _ \\ \ / /| || '_ \  | |_| || | | | / _` | / _` || | / _ \/ __|| __|/ _ \ | '_ \     #
#    | . \|  __/ \ V / | || | | | |  _  || |_| || (_| || (_| || ||  __/\__ \| |_| (_) || | | |    #
#    |_|\_\\___|  \_/  |_||_| |_| |_| |_| \__,_| \__,_| \__,_||_| \___||___/ \__|\___/ |_| |_|    #
#                                                                                                 #
#             ____   ____    _             _____           ____     ___    ____    _____          #
#            / ___| |  _ \  | |   __   __ |___ /          |___ \   / _ \  |___ \  |___ /          #
#           | |  _  | |_) | | |   \ \ / /   |_ \   _____    __) | | | | |   __) |   |_ \          #
#           | |_| | |  __/  | |___ \ V /   ___) | |_____|  / __/  | |_| |  / __/   ___) |         #
#            \____| |_|     |_____| \_/   |____/          |_____|  \___/  |_____| |____/          #
#                                                                                                 #
#                                                                                                 #
###################################################################################################
