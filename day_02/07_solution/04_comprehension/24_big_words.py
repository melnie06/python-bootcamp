# You can use a custom message using input()
sentence = "I like big data and AI models"

# Find all the words with len > 3
words = sentence.split()
big_words = [word for word in words if len(word) > 3]

print(big_words)