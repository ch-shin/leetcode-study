class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(get_max_by_traversing(s),
                   get_max_by_traversing(flip(s[::-1])))


def get_max_by_traversing(s):
    max_len = 0
    open_count = 0
    close_count = 0

    for i in range(len(s)):
        if s[i] == "(":
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            max_len = max(max_len, open_count * 2)

        if close_count > open_count:
            open_count = 0
            close_count = 0
    return max_len


def flip(s):
    new_s = ""
    for char in s:
        if char == "(":
            new_s += ")"
        else:
            new_s += "("
    return new_s

# TODO: try solutions using DP or Stack