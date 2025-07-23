'''
Scenario
The break statement is used to exit/terminate a loop.

Design a program that uses a while loop and continuously asks the user to enter a word unless 
the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." 
should be printed to the screen, and the loop should terminate.

Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
'''

secret_word = "chupacabra"

user_guess = input("Enter a word to guess the Secret Word: ")

while user_guess != secret_word:
    if secret_word == user_guess:
        break
    user_guess = input("Try to still guess!: ")

print("\nYou've successfully left the loop.")
