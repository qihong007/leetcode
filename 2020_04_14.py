'''
设计一个算法，算出 n 阶乘有多少个尾随零。
示例 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
执行用时：24 ms
内存消耗：12.9 MB
'''
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 2的个数肯定小于5的个数，所以尾随零取决于5的个数
        cnt = 0
        divider = 5
        while n // divider:
            cnt += n // divider
            # 计算1~n中为5,25,125...的倍数的个数
            divider *= 5
        return cnt
#别人代码简洁
'''

#尾随零本质是阶乘中“10=2*5的个数”。2的个数肯定小于5的个数，所以尾随零取决于5的个数

class Solution(object):
    def trailingZeroes(self, n):
        num5 = n
        i = 1
        result = 0

        while num5 > 0:
            num5 = n
            # 计算1~n中为5,25,125...的倍数的个数，例如30/5=6，但其实有7个0，因为25 = 5*5，25有两个5
            bignum = pow(5,i)
            result = num5/bignum + result
            i = i + 1
            num5 = num5/bignum
        
        return result
        """
        :type n: int
        :rtype: int
        """
