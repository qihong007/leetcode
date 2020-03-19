'''
设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输入: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

执行用时 :56 ms, 在所有 Python 提交中击败了92.11% 的用户
内存消耗 :20.6 MB, 在所有 Python 提交中击败了100.00%的用户
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#思路：先判断p和q是不是彼此的子树这种情况，接下来从root往下判断，收集同时包含p和q的节点containtwo(self, root, p, q, treelist)，最后包含p和q的节点就是距离最近的祖先节点
class Solution(object):
    def contain(self, p, q, nums):
        if p == None:
            return     
        if p == q:
            index = True
            nums.append(index)
            return
        self.contain(p.left, q, nums)
        self.contain(p.right, q, nums)
            

    def containtwo(self, root, p, q, treelist):
        nums = []
        self.contain(root, p, nums)
        self.contain(root, q, nums)
        print(nums)
        if len(nums) == 2:
            treelist.append(root)
        else:
            return
        self.containtwo(root.left, p, q, treelist)
        self.containtwo(root.right, p, q, treelist)
    

    def lowestCommonAncestor(self, root, p, q):
        
        nums1 = []
        nums2 = []
        self.contain(p, q, nums1)
        self.contain(q, p, nums2)
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > 0:
            return p
        if l2 > 0:
            return q

        treelist = []
        self.containtwo(root, p, q, treelist)

        finalindex = len(treelist)-1
        result = treelist[finalindex]
        return result
