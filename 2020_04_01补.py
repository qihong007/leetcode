'''
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

示例1:

 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0

示例2:

 输入：nums = [1, 1, 1]
 输出：1



执行用时 :24 ms, 在所有 Python 提交中击败了77.89% 的用户
内存消耗 :13.2 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def findMagicIndex(self, nums):
        for i in range(0, len(nums)):
            if i == nums[i]:
                return i
        return -1
