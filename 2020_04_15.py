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
'''

class Solution(object):
    def maxSubArray(self, nums):
        #最笨方法s=
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
