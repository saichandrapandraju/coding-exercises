"""
LeetCode link: https://leetcode.com/problems/valid-palindrome/

Problem description:
--------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

example - 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

example - 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

example - 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    for _ in range(len(s)):
        if l >= r:
            return True
        elif s[l].isalnum() and s[r].isalnum():
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        elif not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1


# test

assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True
