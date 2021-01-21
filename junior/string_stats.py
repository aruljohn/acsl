#
# ACSL Junior Division - String Stats - 2018-2019
# Solution by Arul John
# Problem at http://www.datafiles.acsl.org/samples/contest2/c2-jr-prog.pdf
# Created: 2021-01-20
# Updated: <NEVER>
#

'''
Function to do the string statistics
'''
def string_stats(sentence):
    sentence_lower = sentence.lower() # lower case sentence; we will use it many times

    # Find the number of different letters
    number_of_different_letters = 0
    new_sentence = ''.join(set(sentence_lower))
    # new_sentence has lower case letters
    for x in new_sentence:
        if not 'a' <= x <= 'z': # if current letter x is NOT a letter between 'a' and 'z', remove it
            new_sentence = new_sentence.replace(x, '')
    number_of_different_letters = len(new_sentence)
    print(number_of_different_letters)

    # Find the number of vowels
    number_of_vowels = 0
    vowels_string = 'aeiou'
    for x in sentence_lower:
        if x in vowels_string: # if current letter x is a vowel
            number_of_vowels += 1
    print(number_of_vowels)

    # Find the number of uppercase letters
    number_of_uppercase_letters = 0
    for x in sentence:
        if 'A' <= x <= 'Z': # if current letter x is a letter between 'A' and 'Z'
            number_of_uppercase_letters += 1
    print(number_of_uppercase_letters)

    # Most frequent letter count
    letter_frequency = { }
    for x in sentence_lower:
        if 'a' <= x <= 'z': # if current letter x is a letter between 'a' and 'z'
            if x in letter_frequency:
                letter_frequency[x] += 1 # increase frequency count by 1
            else:
                letter_frequency[x] = 1  # first time, so initialize to 0
    # letter_frequency is a dictionary with key as letter and value as number of occurrences of that letter
    most_frequent_letter_count = max(letter_frequency.values()) # find highest count of occurrences
    print(most_frequent_letter_count)

    # Longest word
    longest_word = ''
    sentence_with_only_letters = sentence
    for letter in sentence_with_only_letters:
        # If x is not A-Z, a-z or space, then remove it
        # meaning, remove it if it's a - or . or comma
        if not ('a' <= letter <= 'z' or 'A' <= letter <= 'Z' or letter == ' '):
            sentence_with_only_letters = sentence_with_only_letters.replace(letter, '')
    # sentence_with_only_letters contains only words and spaces
    # We split it into a list called "words"
    words = sentence_with_only_letters.split(' ')
    # Loop through all words to find the longest word.
    for word in words:
        if len(word) > len(longest_word): # compare the current word with longest word
            longest_word = word           # If the word is longer than the longest word, make longest word take the value of 'word'
    print(longest_word)


# Main
if __name__ == "__main__":
    string_stats('The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.')
    # string_stats('The 2019 All-Star Competition is at Wayne Hills HS in Wayne, New Jersey.')
