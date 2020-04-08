'''
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字不在0和1之间，或者无法精确地用32位以内的二进制表示，则打印“ERROR”。

示例1:

 输入：0.625
 输出："0.101"

示例2:

 输入：0.1
 输出："ERROR"
 提示：0.1无法被二进制准确表示

提示：

    32位包括输出中的"0."这两位。


执行用时 :16 ms, 在所有 Python 提交中击败了83.33% 的用户
内存消耗 :12.6 MB, 在所有 Python 提交中击败了100.00%的用户
'''
class Solution(object):
    def printBin(self, num):
        if num >= 1 or num <= 0:
            return "ERROR"
        s = "0."
        target = num
        while len(s) <= 32:
            target = target * 2
            if target-1 > 0:
                s = s + "1"
                target = target - 1
            elif target-1 < 0:
                s = s + "0"
            else:
                s = s + "1"
                return s
        return "ERROR"
