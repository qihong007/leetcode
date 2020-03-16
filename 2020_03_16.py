'''
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法

示例2:

 输入：n = 5
 输出：13

提示:

    n范围在[1, 1000000]之间


执行用时 :312 ms, 在所有 Python 提交中击败了62.20% 的用户
内存消耗 :12.8 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def waysToStep(self, n):
        
        if n == 1:
            return 1
        if n == 2 :
            return 2
        if n == 3 :
            return 4
        
        result1 = 1
        result2 = 2
        result3 = 4
        num = n
        while num >= 4:
            final = (result1 + result2 +result3)%1000000007
            result1 = result2%1000000007
            result2 = result3%1000000007
            result3 = final%1000000007
            num = num - 1
            
        return final
