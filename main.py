# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = list(word)
    anagram = list(anagram)

    for char in word:
        if char in anagram:
            word.remove(char)
            anagram.remove(char)
        else:
            return False
    return True

