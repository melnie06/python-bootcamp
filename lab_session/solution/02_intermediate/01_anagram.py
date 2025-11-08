from collections import Counter


def anagram(first: str, second: str) -> bool:
    """
    Returns True if the first and second words are anagrams.

    Note: 'Listen' and 'Silent' are anagrams (case-insensitive).
    """
    return Counter(first.lower()) == Counter(second.lower())


print(anagram("listen", "silent"))  # True
print(anagram("Listen", "Silent"))  # True
print(anagram("evil", "vile"))  # True
print(anagram("evil", "vill"))  # False
print(anagram("elvis", "lives"))
print(anagram("a", "aaa"))  # False
