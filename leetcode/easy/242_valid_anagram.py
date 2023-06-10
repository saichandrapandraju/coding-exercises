"""
LeetCode link: https://leetcode.com/problems/valid-anagram/

Problem description:
--------------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


example - 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

example - 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
"""

from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    s_counts = defaultdict(int)
    t_counts = defaultdict(int)
    
    # count all the characters in 's'
    for i in range(len(s)):
        s_counts[s[i]]+=1
    
    # count all the characters in 't'
    for j in range(len(t)):
        t_counts[t[j]]+=1
    
    # compare counts of intersection chars and length for same chars
    for k, v in s_counts.items():
        if k in t_counts and v==t_counts[k]:
            continue
        return False            # either a specific char not in t or count doesn't match, not anagram
    return len(s_counts) == len(t_counts)
    


# test

assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
assert isAnagram(" ", "") == False
assert isAnagram("  ", " ") == False
assert isAnagram("", "") == True
