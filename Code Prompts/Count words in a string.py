# Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.
import collections
file = open("C:/Users/André/OneDrive/School/Python/Projects/Code Prompts/words.txt","r")
words = file.read()
file.close()
count = words.split(" ")

print(count)
print(len(count))