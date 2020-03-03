'''
Given a string, write a function to check if it is a permutation of a palin­ drome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.

给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词。

Example1:

Input: "tactcoa"
Output: true（permutations: "tacocat"、"atcocta", etc.）


'''


class Solution(object):
    def canPermutePalindrome(self, s):
        x = set(s)
        list1 = []
///先用set，计算每个字母出现几次
        for cha0 in x:    
            i = 0 
            for cha1 in s:
                if cha0 == cha1:
                    i = i + 1
            list1.append(i)
///接着以回文为例，如果构成回文，则个位数为偶数的字符串所有字符出现次数都可以被2整除，记录下不能被2整除的个数
        num = 0
        for index in list1:
            if index%2 == 1:
                num = num + 1
///接着以回文为例，如果构成回文，则个位数为偶数的字符串所有字符出现次数都可以被2整除，记录下不能被2整除的个数
///如果都能整除，则肯定是回文；不能整除时，如果只有一个不能整除且字符串长度为奇数，也可判断为回文
        if num == 0:
            return True
        if (num == 1) & (len(s)%2 == 1):
            return True
        print(num)       

        return False 


            
        """
        :type s: str
        :rtype: bool
        """
'''
执行用时 :20 ms, 在所有 Python 提交中击败了66.67% 的用户
内存消耗 :11.9 MB, 在所有 Python 提交中击败了100.00%的用户
'''
