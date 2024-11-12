from collections import Counter

# 1. Count the characters in text
text = str(input("Enter the text: "))
res = Counter(text)
print("Count of all characters in", text, "is:\n", res)

# 2. Add "ing" and "ly"
def modi(s):
    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

word = str(input("Enter the word: "))
print("Modified word:", modi(word))

# 3. Find the longest word
n = int(input("Enter the number of words: "))
list1 = []

print("Enter the words:")
for i in range(n):
    c = input()
    list1.append(c)

print("The original list:", list1)

long_word = max(list1, key=len)
length = len(long_word)

print("Maximum length string is:", long_word, "with length:", length)
