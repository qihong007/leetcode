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

题解思路：
第一层递归遍历每个节点，第二层递归遍历每个每个结点开始的路径
此处撰写解题思路
话说，这个题坑还是不少，(可能也是我有时候写递归结束条件不严谨，有些想当然)不过啊，总算过了。好了来说一说做这题的思路吧。首先题目强调路径不一定经过根节点.so...我们就先从根节点出发，把以根节点出发的路径都找到.嗯...我想过依据target<0来剪枝，其实这一步就发现了结点里面的值有可能是负的（想出这个测试用例的人真是个小机灵鬼）算了，放弃剪枝了，先用暴力法求出来把。然后根节点出发的dfs就写出来了。
接下来，就是遍历树里面每一个根节点。因为路径可能是从任何一个结点出发的.
纯暴力解法，不带一点优化。

'''

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def path(self, root, sum):
        #这里是root是否为None
        if not root:
          
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.path(root.left, sum - root.val)
        res += self.path(root.right, sum - root.val)
        return res
