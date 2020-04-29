'''
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]


执行用时 :236 ms, 在所有 Python 提交中击败了47.14% 的用户
内存消耗 :15.4 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def path(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.path(root.left, sum - root.val)
        res += self.path(root.right, sum - root.val)
        return res
