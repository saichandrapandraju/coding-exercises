"""
LeetCode link: https://leetcode.com/problems/longest-palindrome/

Problem description:
--------------------
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

example - 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

example - 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.
    
Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
"""

def longestPalindrome(s: str) -> int:
    mem = set()     # store new char
    length = 0
    for c in s:     # O(n)
        if c in mem:        # if char repeats, these 2 instances can be added to longest palindrome, so increment by 2
            length+=2
            mem.remove(c)   # remove the char as we added it to the length
            
        else:
            mem.add(c)      # if not seen till now, store in mem
    return length+1 if mem else length      # if mem is not empty(none of them are repeated), add 1 to length b/c we can take any one element from the set and add it to center of palindrome string. if mem is empty, return current length.

    
# test
assert longestPalindrome("abccccdd") == 7
assert longestPalindrome("aA") == 1
assert longestPalindrome("a") == 1
assert longestPalindrome("aaaaa") == 5
assert longestPalindrome("baaaa") == 5
assert longestPalindrome("aaaaaaaabb") == 10
