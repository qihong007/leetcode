'''
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:

 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2

示例2:

 输入：A = 1，B = 2
 输出：2

执行用时 :24 ms, 在所有 Python 提交中击败了50.00% 的用户
内存消耗 :12.8 MB, 在所有 Python 提交中击败了100.00%的用户

解题思路

1.Python3 中的整型是补码形式存储的
2.Python3 中 bin 一个负数（十进制表示），输出的是它的原码的二进制表示加上个负号
3.所以你为了获得负数（十进制表示）的补码，需要手动将其和十六进制数 0xffffffff 进行按位与操作，得到结果是个十六进制数，再交给 bin() 进行输出，得到的才是你想要的补码表示。
'''


class Solution(object):
    

    def convertInteger(self, A, B):
        '''
        简便代码
        if A == B:
            return 0
        if A < 0:
            A &= 0xffffffff
        if B < 0:
            B &= 0xffffffff
        return str(bin(A ^ B)).count("1")


        '''
        #这一步是为了应对负数
        if A < 0:
            A &= 0xffffffff
        if B < 0:
            B &= 0xffffffff
        #print(bin(c),bin(a))
        if A == B:
            return 0
        lenA = len(bin(A))
        lenB = len(bin(B))
        num = abs(lenA-lenB)
        s =  "0"
        for i in range(0,num-1):
            s = s + "0"
            
        strA = bin(A)
        strB = bin(B)
        print(lenA, lenB)
        print(s, len(s))
        final = 0
        if lenA > lenB:
            newA = strA[2:]
            newB = s + strB[2:]
            print(len(newB), len(newA))
            for i in range(0, len(newA)):
                if newA[i] != newB[i]:
                    final = final + 1
        elif lenA == lenB:
            newA = strA[2:]
            newB = strB[2:]
            for i in range(0, len(newA)):
                if newA[i] != newB[i]:
                    final = final + 1

        elif lenA < lenB:
            newB = strB[2:]
            newA = s + strA[2:]
            print(len(newB), len(newA))
            for i in range(0, len(newA)):
                if newA[i] != newB[i]:
                    final = final + 1

        return final
        
