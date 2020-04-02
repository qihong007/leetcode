'''
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

示例1:

 输入：A = 1, B = 10
 输出：10

示例2:

 输入：A = 3, B = 4
 输出：12

提示:

    保证乘法范围不会溢出


执行用时 :24 ms, 在所有 Python 提交中击败了28.92% 的用户
内存消耗 :12.9 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def multiply(self, A, B):
        if B == 0:
            return 0
        if A == 0:
            return 0
        B = B - 1

        return A + self.multiply(A,B)
