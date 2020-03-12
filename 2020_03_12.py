'''
Implement a function to check if a linked list is a palindrome.
查查是不是回文
 

Example 1:

Input:  1->2
Output:  false 

Example 2:

Input:  1->2->2->1
Output:  true 


'''
class Solution(object):
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True

        '''
        if head == None or head.next == None:
        而不是if head == None | head.next == None:
        '''
        num = 0
        p0 = head
        p1 = head
        p2 = head

        while head != None:
            num = num + 1
            head = head.next

        first = num/2
        l1 = []
        for i in range(0, first):
            l1.append(p1.val)
            p1 = p1.next
        l2 = []
        if num%2 == 0:
            for i in range(0, first):
                l2.append(p1.val)
                p1 = p1.next
        else:
            p1 = p1.next
            for i in range(0, first):
                l2.append(p1.val)
                p1 = p1.next

        print(l1)
        l2 = list(reversed(l2))
        
        return l1 == l2
