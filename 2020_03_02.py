'''
Given two strings,write a method to decide if one is a permutation of the other.

Example 1:

Input: s1 = "abc", s2 = "bca"
Output: true

Example 2:

Input: s1 = "abc", s2 = "bad"
Output: false

Note:

    0 <= len(s1) <= 100
    0 <= len(s2) <= 100
'''

class Solution(object):

    def CheckPermutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        s = ord(s1[0])
        for i in range(1, len(s1)):
            s = ord(s1[i])^s
        for j in range(0, len(s2)):
            s = ord(s2[j])^s
        if s == 0:
            if sorted(s1) == sorted(s2): 
                return True
        return False

'''
执行用时 :16 ms, 在所有 Python 提交中击败了88.00% 的用户
内存消耗 :11.8 MB, 在所有 Python 提交中击败了100.00%的用户
这种方法存在一个问题，就是s1 = aa, s2 = bb 会存在误报.我的解决思路是，先用时间复杂度O(N)看^是否为truetrue，再用排序核实一下
'''
