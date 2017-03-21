# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

import collections

Vowels = "aeiouAEIOU"
count = 0
text = input("Write your text here:  ")
c = collections.Counter(text)

for i in text:
    if i in Vowels:
        print("%s : %d" % (i, c[i]))
        count += 1
print(count)