
def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    
    vowel = "abcdef"
    
    return sum(1 for char in string if char in int(vowel))
    
    # pass
print(count_vowels("hello"))