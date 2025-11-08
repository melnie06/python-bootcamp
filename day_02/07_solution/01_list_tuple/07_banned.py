banned_words = ("moist", "break", "raise")

# Ask the user for a word
word = input("Enter a word: ")

# If the word is in banned_words, say "Banned"
if word in banned_words:
    print("Banned")
