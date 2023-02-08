# Given a list of words, write a program to find the longest word made of other words in the list

# Input: cat, banana, dog, nana, walk, walker, dogwalker
# Output: dogwalker

def main(words):
    # Sort the list of words by length
    words.sort(key=len, reverse=True)
    # Iterate through the list of words
    for word in words:
        # Check if the word can be made up of other words in the list
        if canMakeWord(word, words):
            # If it can, print the word
            print(word)
            return
    # If no word can be made up of other words, print an error message
    print("No word found")

def canMakeWord(word, words):
    # If the word is in the list of words, it can be made up of other words
    if word in words:
        return True
    # Iterate through the word
    for i in range(1, len(word)):
        # Split the word into two parts
        left = word[:i]
        right = word[i:]
        # Check if the left part can be made up of other words
        if canMakeWord(left, words):
            # If it can, check if the right part can be made up of other words
            if canMakeWord(right, words):
                # If it can, return True
                return True
    # If the word can't be made up of other words, return False
    return False

if __name__ == "__main__":
    words = ["cat", "banana", "dog", "catwalker", "nana", "walk", "walker", "bananacatdog", "dogwalker"]
    # output = "bananacatdog"
    main(words)
