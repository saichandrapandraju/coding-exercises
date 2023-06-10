"""
LeetCode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem description:
--------------------
Given a string s, find the length of the longest substring without repeating characters.

example - 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

example - 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

example - 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:
    mem = set()     # take a set so that operations are O(1)
    l = 0           # initialize left pointer to 0
    out = 0         # initialize max_length to 0
    for r in range(len(s)):         # iterate right pointer from start
        if s[r] not in mem:         # if cur item not in mem, add it
            mem.add(s[r])           
        else:                       # if cur item in mem, remove items from the left till the cur element instance is no longer in mem
            while s[r] in mem:
                mem.remove(s[l])    # remove takes value(b/c sets don't have index/order), we start from left to remove in order
                l+=1                # remove from left to right
            mem.add(s[r])           # once we remove till the repeated character, add the curr element
        out = max(out, len(mem))    # regarless of above ops, update max_length
    return out


    
# test

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("pwwkewabcabcbb") == 6
