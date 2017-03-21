# Enter a string and the program will reverse it and print it out.

def reverseText(string):
    newstring = string[::-1]
    return newstring

MyString = input("Write your text to be reversed:  ")
thisshit = reverseText(MyString)
print(thisshit)