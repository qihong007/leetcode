'''
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2

示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null




执行用时 :80 ms, 在所有 Python 提交中击败了28.13% 的用户
内存消耗 :20.7 MB, 在所有 Python 提交中击败了100.00%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#备注，本题先用中序遍历获得数组，接着判断目标是否大于等于数组的最大值，如果目标大于等于，说明这个数不在数组里面
#如果小于，用搜索算出目标的下一个值是什么，然后再去root这棵树找这个节点
#思考：这个办法太笨了，时间复杂度很高，且步骤复杂：中序遍历-搜索数组-搜索二叉树，
#希望能有一个遍历的同时找出下一个的算法

class Solution(object):
    def zhongxu(self, node, nums):
        if node == None:
            return
        self.zhongxu(node.left, nums)
        nums.append(node.val)
        self.zhongxu(node.right, nums)
    
    def search(self, node, target):
        if node == None:
            return None
        while node != None:
            if target == node.val:
                return node
            elif target > node.val:
                node = node.right
            elif target < node.val:
                node = node.left
        return None

    def inorderSuccessor(self, root, p):
        nums = []
        self.zhongxu(root, nums)
        length = len(nums)
        maxnum = nums[length-1]
        if p.val >= maxnum:
            return None
        node = TreeNode(0)
        target = p.val

        for i in nums:
            if i > p.val:
                target = i
                break       
        
        node = self.search(root, target)
      
        return node
