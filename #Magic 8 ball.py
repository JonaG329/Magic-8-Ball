#Magic 8 ball
#Jonathan Garcia
#1/19/24

#Functions
print("Welcome to 8-Ball")

import random #a feature that allows the randomization of the responses

responses = ["It is certain", "For sure!", "Yes definitely", "Most likely", "Probably", "Ask again later", "Better not tell you now", "Don't count on it", "My sources say no", "Hell nah", "Lame ahh question" ] #these are reponses that the 8-ball could say

while True:
    question = input("What is your question for the 8-Ball?: ")
    x = question.endswith("?") #makes sure the question from the user contains a question mark at the end
    if x == True:
        option = input("Do you want to shake the eight ball? \nEnter yes or y OR no or n: ") #user is prompted to answer the question and respond given 4 choices
        if (option == "yes") or (option == "y"):
         print(random.choice(responses))
        if (option == "no") or (option == "n"):
            print("Thanks for playing.")
            break #exits  the program
    if x == False:
        print("Please enter a question mark at the end of your question.") #if question does not have a question mark at the end, user needs to input the question again


    

