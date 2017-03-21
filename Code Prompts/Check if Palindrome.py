# Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”

word = input("enter a palindrome:  ")

if word[::-1] == word:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")