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
    l, r = 0, len(s) - 1            # set two pointers for left most and right most characters
    for _ in range(len(s)):         # iterate len(s) times, will work b/c each time we'll be incrementing/decrementing by one position
        if l >= r:                  # terminating condition
            return True             # if left pointer reaches/crosses right pointer -> all the chars till that point are valid -> so True
        elif s[l].isalnum() and s[r].isalnum():         # if both chars are valid alpha numerics
            if s[l].lower() == s[r].lower():            # if both are equal, increment left and decrement right to progress further
                l += 1
                r -= 1
            else:
                return False                            # if both are valid chars and not equal -> not palindrome
        elif not s[l].isalnum():                        # if left is not proper valid char -> increment left
            l += 1
        elif not s[r].isalnum():                        # if right is not proper valid char -> decrement right
            r -= 1


# test

assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True
