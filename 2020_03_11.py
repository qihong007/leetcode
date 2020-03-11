'''
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912

执行用时 :80 ms, 在所有 Python 提交中击败了44.90% 的用户
内存消耗 :12.8 MB, 在所有 Python 提交中击败了100.00%的用户

执行用时 :80 ms, 在所有 Python 提交中击败了41.82% 的用户
内存消耗 :32.7 MB, 在所有 Python 提交中击败了100.00%的用户
'''
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        print(l1.val, l2.val)
        list1 = l1
        list2 = l2
        num1 = 0
        num2 = 0
        i1 = 0
        i2 = 0

        while list1 != None:
            num1 = num1 + list1.val * pow(10, i1)
            i1 = i1 + 1
            list1 = list1.next
        
        while list2 != None:
            num2 = num2 + list2.val * pow(10, i2)
            i2 = i2 + 1
            list2 = list2.next
        
        num3 = num1 + num2
        print(num3)
        
        #当结果为个位数时
        if num3 < 10:
            return ListNode(num3)

        #错误写法如下，a.next此时为None
        #a = ListNode(0) 
        #b = ListNode(2)  
        #b = a.next
        #这样会报错
        '''
        正确写法
        a =  ListNode(0)
        b =  ListNode(2)
        a.next = b
        '''
        head = ListNode(0)
        p = head       
        while (num3/10 != 0) | (num3 > 0) :
            print(num3)
            head.next = ListNode(num3%10)       
            head = head.next
            num3 = num3/10 

        return p.next
