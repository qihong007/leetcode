'''
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：

输入: numbers = [1,2]
输出: [2,1]

执行用时 :16 ms, 在所有 Python 提交中击败了89.19% 的用户
内存消耗 :12.7 MB, 在所有 Python 提交中击败了100.00%的用户

'''


class Solution(object):
    #还有位运算可以参考一下
    def swapNumbers(self, numbers):
        #方法一：有点作弊
        '''
        b = []
        b.append(numbers[1])
        b.append(numbers[0])
        return b
        '''
        #方法二：
        numbers[0] = numbers[0] + numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers
