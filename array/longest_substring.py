# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

# Sliding window problem

def lengthOfLongestSubstring(self, s):
    cset = set()
    res = 0

    l = 0
    r = 0

    while r < len(s):
        while s[r] in cset:
            cset.remove(s[l])
            l += 1
        cset.add(s[r])
        res = max(res, r - l + 1)
        r += 1
    return res
