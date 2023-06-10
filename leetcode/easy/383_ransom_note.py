"""
LeetCode link: https://leetcode.com/problems/ransom-note/

Problem description:
--------------------
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

example - 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

example - 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

example - 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""

from collections import defaultdict

def canConstruct(ransomNote: str, magazine: str) -> bool:
    r_counts = defaultdict(int)
    m_counts = defaultdict(int)
    
    # count all the characters in 'ransomNote'
    for i in range(len(ransomNote)):
        r_counts[ransomNote[i]]+=1
    
    # count all the characters in 'magazine'
    for j in range(len(magazine)):
        m_counts[magazine[j]]+=1
    
    # count of chars in ransom should be <= respective counts in magazine
    for k, v in r_counts.items():
        if k in m_counts and v<=m_counts[k]:
            continue
        return False            # either a specific char not in magazine or required ransom count is more than available magazine, couldn't construct
    return True
    


# test

assert canConstruct("anagram", "nagaram") == True
assert canConstruct("rat", "car") == False
assert canConstruct("rat", "cart") == True
assert canConstruct(" ", "") == False
assert canConstruct("  ", " ") == False
assert canConstruct("", " ") == True
assert canConstruct(" ", "") == False
assert canConstruct("a", "b") == False
assert canConstruct("aa", "ab") == False
assert canConstruct("aa", "aab") == True
