'''
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)

示例2:

 输入：num = 3
 输出：3

提示:

    num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。

执行用时 :20 ms, 在所有 Python 提交中击败了60.34% 的用户
内存消耗 :12.7 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    def getresult(self, newstr, sin, dou):
        #将奇数位和偶数位分开
        for i in range(0, len(newstr)):
            if i%2 == 0:
                dou = dou + newstr[i]
            else:
                sin = sin + newstr[i]
        #将字符串重新组织，倒换奇数位和偶数位
        newstring = "" 
        for i in range(0, len(sin)):
            newstring = newstring + sin[i] + dou[i]
        return int(newstring,2)

    def exchangeBits(self, num):
        newstr = bin(num)[2:]
        sin = ""
        dou = ""
        if len(newstr)%2 == 0:
            return self.getresult(newstr, sin, dou)
        else:
            newstr = "0" + newstr
            return self.getresult(newstr, sin, dou)
