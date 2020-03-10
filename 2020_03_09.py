'''
Implement an algorithm to find the kth to last element of a singly linked list. Return the value of the element.

Note: This problem is slightly different from the original one in the book.

Example:

Input:  1->2->3->4->5 和 k = 2
Output:  4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
执行用时 :36 ms, 在所有 Python 提交中击败了21.98% 的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def kthToLast(self, head, k):
        result = head
        num = 0
        while head != None:
            num = num + 1
            head = head.next
        if num == 1:
            return result.val
        for i in range(0, num-k):
            result = result.next
            '''
            final = result.val
            '''
        '''
        方法二，容易理解的思路
        for i in range(0, num-k+1):
            final = result.val
            result = result.next

        return final
        '''
        return result.val
