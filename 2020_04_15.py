'''
给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解


执行用时 :8652 ms, 在所有 Python 提交中击败了5.79% 的用户
内存消耗 :13.8 MB, 在所有 Python 提交中击败了100.00%的用户

'''

'''
######
        #动态规划，找出n-1里面最大值，再n大还是n加n-1的最大值大
        #dp[i]为算上了num[i]的最大值，所以相当于在i位置包含了第i个数的最大值
        
        执行用时 :28 ms, 在所有 Python 提交中击败了76.32% 的用户
        内存消耗 :13.8 MB, 在所有 Python 提交中击败了100.00%的用户
    def maxSubArray(self, nums):
        dp = []
        for i in range(0, len(nums)):
            dp.append(0)
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
            result = max(result, dp[i])
        return result  

'''

class Solution(object):
    def maxSubArray(self, nums):
        #最笨方法暴力算每个位置的最大值
        maxnum = nums[0]
        sumnum = 0
        for i in range(0, len(nums)):
            sumnum = nums[i]
            if i == len(nums)-1 and nums[i] > maxnum:
                maxnum = sumnum
                break

            if sumnum > maxnum:
                maxnum = sumnum
            
            for j in range(i+1, len(nums)):
                sumnum = sumnum + nums[j]
                if sumnum > maxnum:
                    maxnum = sumnum
        return maxnum
