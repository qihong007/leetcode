'''
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \ 
      2    3
     / \    \ 
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]


执行用时 :28 ms, 在所有 Python 提交中击败了35.00% 的用户
内存消耗 :12.6 MB, 在所有 Python 提交中击败了100.00%的用户
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #这一步求树的最大深度
    def maxdep(self, tree):
        if tree == None:
            return 0
        left = self.maxdep(tree.left)
        right = self.maxdep(tree.right)
        num = 0
        if left > right:
            num = left
        else:
            num = right
        return num+1
    
    #这一步把每一层的结果输入
    def getresult(self, tree, num, result):
        if tree == None:
            return
        new = ListNode(tree.val)
        node = result[num]
        #为链表增添新的值
        while node != None:
            if node.next == None:
                node.next = new
                break
            node = node.next
        num = num + 1
        left = self.getresult(tree.left, num, result)
        right = self.getresult(tree.right, num, result)
        return
        

    def listOfDepth(self, tree):
        num = self.maxdep(tree)
        result = []
        #这一步创造每一层的空间
        for i in range(0, num):
            node = ListNode(0)
            result.append(node)
        #print(result[0].val)
        index = 0
        #将每一层的内容输入到对应的位置，eg：第0层输入result[0],第1层输入result[1]
        self.getresult(tree, index, result)
        #第一个结果是0，next才是想要的值
        for i in range(0, num):
            result[i] = result[i].next
        return result
