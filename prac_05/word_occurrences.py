"""
CP1404 Practical 05
"""

text = input("Text: ")
words = text.split()
word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

# Sort alphabetically by word
words = sorted(word_to_count.keys())

max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
