'''
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

就是简单的删除结点，由于函数给出的是被删除的结点 直接将它的下一个结点复制给要被删除的结点，删除下一个结点 借鉴别人的思路

Example:

Input: the node c from the linked list a->b->c->d->e->f
Output: nothing is returned, but the new linked list looks like a->b->d->e->f



执行用时 :32 ms, 在所有 Python 提交中击败了37.86% 的用户
内存消耗 :13.2 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

        
       

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
