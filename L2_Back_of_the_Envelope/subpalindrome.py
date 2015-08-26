# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficiency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

import itertools


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if text == '':
        return (0, 0)
    combo = [c for c in itertools.combinations(list(range(len(text))), 2) if c[0] < c[1]]
    solutions = []
    for c in combo:
        start = c[0]
        end = c[1]
        originalText = text[start: end+1]
        reversedText = textReverse(originalText)
        if originalText.lower() == reversedText.lower():
            solutions.append(c)
    if solutions == []:
        return None
    longest = (0, 0)
    for s in solutions:
        if (s[1]+1-s[0]) > (longest[1]-longest[0]):
            longest = (s[0], s[1]+1)
    return longest


def textReverse(text):
    outText = ''
    for i in xrange(len(text)-1, -1, -1):
        outText += text[i]
    return outText


def grow(text, start, end):
    while start > 0 and end < len(text) and text[start-1].upper() == text[end].upper():
        start -= 1
        end += 1
    return (start, end)


def longest_subpalindrome(text):
    if text == '':
        return (0, 0)
    def length(slice):
        a, b = slice
        return (b-a)
    candidates = [grow(text, start, end) for start in range(len(text)) for end in (start, start+1)]
    return max(candidates, key=length)


def test():
    L = longest_subpalindrome_slice
    L1 = longest_subpalindrome
    assert L('racecar') == (0, 7)
    assert L1('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L1('Racecar') == (0, 7)
    assert L1('RacecarX') == (0, 7)
    assert L1('Race carr') == (7, 9)
    assert L1('') == (0, 0)
    assert L1('something rac e car going') == (8,21)
    assert L1('xxxxx') == (0, 5)
    assert L1('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()