'''
如果数组中多一半的数都是同一个，则称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5

 

示例 2：

输入：[3,2]
输出：-1

 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2


执行用时 :36 ms, 在所有 Python 提交中击败了64.00% 的用户
内存消耗 :15.2 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    def majorityElement(self, nums):
        result = sorted(nums)
        target = result[len(nums)/2]
        index = 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                index = index + 1
        if index < len(nums)/2:
            return -1
        else:
            return target
