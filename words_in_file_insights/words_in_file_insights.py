import sys, re
from collections import Counter

# load text from file and clean
filename = sys.argv[1]
with open(f'{filename}.txt', 'r') as file:
    text = file.read()
text = text.lower()
words_raw = re.findall('[a-zA-Z]{3,}', text)

# returns True if word is a palindrome
def is_palindrome(word):
    return(word == word[::-1])


# returns True if word is an isogram
def is_isogram(word):
    return(Counter(word).most_common()[0][1] == 1)


# find types of words in text
tautonyms = set(re.findall('([a-zA-Z]{2,})-\1', text))
palindromes = set([word for word in words_raw if is_palindrome(word) and len(word) >= 3])
isograms = set([word for word in words_raw if is_isogram(word) and len(word) >= 8])
really_long_words = set([word for word in words_raw if len(word) >= 12])

# print results
print('\n********************************************************************')
print(f'An analysis of types of words found in file: {filename}.txt')
print('********************************************************************')
print(f'\nNumber of Palindromes (len >= 3): {len(palindromes)}\n\n{palindromes}')
print(f'\nNumber of Isograms (len >= 8): {len(isograms)}\n\n{isograms}')
print(f'\nNumber of long words (len >= 12): {len(really_long_words)}\n\n{really_long_words}')
print(f'\nNumber of Tautonyms: {len(tautonyms)}\n\n{tautonyms}')
