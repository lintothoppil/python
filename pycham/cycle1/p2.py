print("Linto Mathew Joy")
print("A24MCA041")
print("Experiment No: 2")

from collections import Counter


text = input("Enter the line of text: ")
words = text.lower().split()
word_count = Counter(words)


for word, count in word_count.items():
    print(f"{word} appears {count} times")


if words:
    first_word = words[0]
    if len(first_word) > 1:

        first_word = first_word[-1] + first_word[1:-1] + first_word[0]
        print(f"The swapped word is: {first_word}")
    else:
        print("Cannot swap the first letter of a single-letter word.")
else:
    print("No words to process.")
