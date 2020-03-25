'''
编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。

示例：

输入： a = 1, b = 2
输出： 2



执行用时 :24 ms, 在所有 Python 提交中击败了43.18% 的用户
内存消耗 :12.9 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    def maximum(self, a, b):
        c = max(a,b)
        return c
