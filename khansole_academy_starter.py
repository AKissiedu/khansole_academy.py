"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

# successful_attempts is a counter that keeps track of successful attempts made

successful_attempts = 0

# the while loop executes until three consecutive correct answers have been provided.
# first_number and second_number are variables that hold randomly generated integers between 10 and 99.
# answer is also a variable that holds the sum of the two randomly generated numbers.

while successful_attempts < 3:
    first_number = random.randint(10, 99)
    second_number = random.randint(10, 99)
    correct_answer = first_number + second_number

    # The user is asked to evaluate the sum of the two numbers using the input function
    # and the result is stored as user_name

    user_answer = input("What is {} + {} ? : ".format(first_number, second_number))

    # using the if/else statement, the answer from the user is converted to integer and compared with the right answer

    if int(user_answer) == correct_answer:
        successful_attempts += 1
        print("Your answer: {}".format(user_answer))
        print("Correct! You've gotten {} correct in a row".format(successful_attempts))
    else:
        print("Your answer: {}".format(user_answer))
        print("Incorrect answer. The expected answer is: {}\n".format(correct_answer))
        successful_attempts = 0
print("Congratulations! You mastered addition")