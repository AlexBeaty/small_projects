import sys, re
from collections import Counter

filename = sys.argv[1]
with open(f'{filename}.txt', 'r') as file:
    text = file.read()


def is_isogram(word):
    return(Counter(word).most_common()[0][1] == 1)

words_raw = re.findall('[a-zA-Z]{3,}', text)
palindromes = set([word.lower() for word in words_raw if word.lower() == word[::-1].lower() and len(word) >= 3])
long_isograms = set([word.lower() for word in words_raw if is_isogram(word.lower()) and len(word) >= 8])
really_long_words = set([word.lower() for word in words_raw if len(word) >= 12])

print(f'\n\nPalindromes of length 3+:\n\n{palindromes}')
print(f'\nIsograms of length 8+:\n\n{long_isograms}')
print(f'\nWords of length 12+:\n\n{really_long_words}')
