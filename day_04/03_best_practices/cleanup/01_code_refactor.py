def count_words_with_vowel(text):
    words = text.split()

    words_with_vowels_count = 0
    vowels = "aeiou"

    for word in words:
        if any(vowel in words for vowel in vowels):
            words_with_vowels_count += 1

    return words_with_vowels_count
