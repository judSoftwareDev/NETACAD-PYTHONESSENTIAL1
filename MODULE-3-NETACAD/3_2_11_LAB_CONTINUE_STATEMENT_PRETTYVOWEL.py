'''
Scenario
Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab and create a better, 
upgraded (pretty) vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about 
string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. Use concatenation 
operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.

Test your program with the data we've provided for you.
'''


word_without_vowels = ""

user_word = input("Enter a word that has Vowels: ")
user_word = user_word.upper()


for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)
