'''
Given a sorted (increasing order) array with unique integer elements, write an algo­rithm to create a binary search tree with minimal height.

Example:

Given sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5]，which represents the following tree: 

          0 
         / \ 
       -3   9 
       /   / 
     -10  5 

来源：力扣（LeetCode）

类调用自己的函数记得用self
执行用时 :48 ms, 在所有 Python 提交中击败了42.05% 的用户
内存消耗 :17.2 MB, 在所有 Python 提交中击败了100.00%的用户

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getNode(self,low, high, num):
        if low < 0 or low > high: 
            return None
        mid = low + (high - low)/2
        val = num[mid]
        node = TreeNode(val)
        node.left = self.getNode(low, mid-1, num)
        node.right = self.getNode(mid+1, high, num)
        return node


    def sortedArrayToBST(self, nums):
        if len(nums) < 1:
            return None
        low = 0
        high = len(nums)-1
        mid = low + (high - low)/2
        val = nums[mid]
        print(val)
        root = TreeNode(val)
        root.left = self.getNode(low, mid-1, nums)
        root.right = self.getNode(mid+1, high, nums)
        return root
