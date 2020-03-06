'''
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 (e.g.,"waterbottle" is a rotation of"erbottlewat"). Can you use only one call to the method that checks if one word is a substring of another?

Example 1:

Input: s1 = "waterbottle", s2 = "erbottlewat"
Output: True

Example 2:

Input: s1 = "aa", "aba"
Output: False


执行用时：16 ms
内存消耗：12.2 MB
'''
class Solution(object):
    def isFlipedString(self, s1, s2):
        
        '''
        方法一，排序后比较
        if len(s1) != len(s2):
            return False
        str1 = sorted(s1)
        str2 = sorted(s2)
        if str1 == str2:
            return True
        else:
            return False
        '''
        '''
        1.如果两个字符串长度不相等，那一定不是轮转字符，返回False
        2.长度相等，如果是轮转字符，将其中一个字符两次相加，其中一定包含另一个字符。
        '''
        if len(s1) != len(s2):
            return False
        str1 = s1 + s1
        if s2 in str1:
            return True
        else:
            return False
