# from collections import counter

def is_anagram(word1, word2):
    # word1 = "silent"
    # word2 = "listen"
    w1  = word1.lower()
    w2  = word2.lower()

# def is_anagram("listen", "silent"):
    
    if len(w1) != len(w2):
        return False
    
    for letter in w1:
        if w1.count(letter) != w2.count(letter):
            return False
    # pass
    return True

# # test 1:

def test_is_anagram_true():
    # assert is_anagram(w1, w2) == True
    assert is_anagram("silent", "listen") == True
    
def test_is_anagram_edge():
    # assert is_anagram(w1, w2) == True
    assert is_anagram("aaa", "aab") == True
    
    
# # test 2:
def test_is_anagram_false():
    assert is_anagram ("face", "save") == False

# # def is_palindrome(word1, word2):
#     pass


# def is_pangram(word):
#     pass


# listen