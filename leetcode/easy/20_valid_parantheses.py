'''
LeetCode link: https://leetcode.com/problems/valid-parentheses/

Problem description:
--------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

example - 1:
    Input: s = "()"
    Output: true

example - 2:
    Input: s = "()[]{}"
    Output: true

example - 3:
    Input: s = "(]"
    Output: false

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
'''


def isValid(s: str) -> bool:
    mapping = { ")" : "(",
                "]" : "[",
                "}" : "{" }    
    stack = []
    
    for char in s:      # one iteration -> O(n)
        if char in mapping:     # check if cur char is a closing one
            if not stack or stack.pop()!=mapping[char]: return False    # if yes, check if the last added char is the opening counterpart to make it valid. If stack is empty or invalid opening pair, return false
        else:
            stack.append(char)          # if opening one, just add it to stack
            
    return len(stack)==0        # at the end stack should be empty, all opening symbols should have respective closing ones
    


# test
assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("]") == False
assert isValid("[") == False
assert isValid("()[]{") == False
assert isValid("") == True