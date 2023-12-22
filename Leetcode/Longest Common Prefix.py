'''https://leetcode.com/problems/longest-common-prefix/'''

import os

class Solution(object):
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)
        