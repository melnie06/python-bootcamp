def get_longest_word(text):
    longest_word = ""
    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word
t
    return longest_word


print(get_longest_word("The quick brown fox jumps"))
print(get_longest_word("I love programming in Python!"))
print(get_longest_word(""))
