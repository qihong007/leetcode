'''
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：

输入: num = 1775(110111011112)
输出: 8

示例 2：

输入: num = 7(01112)
输出: 4


本题思路很直接，就是直接尝试将数字中的每一位0尝试变成1，然后统计最大值就行了
注意到每一个0位都可以找到对应的一对{x, y}值，x和y分别表示这个0左边和右边连续1的数量，可以为0.
例如：

    111011 => {3, 2}
    0111 => {0, 3}
    1110 => {3, 0}
    1100 => {2, 0}

易知，对于每个为0的数位，将其变成1后能得到的最大连续1的数量为x + y + 1。
我们也不难发现这是一遍扫描就能完成的统计。

最后说一下实现时候需要注意的细节：

    位运算的时候，用右移，因为最后会有一个很大的测试例，左移的话得开一个long long，显然这不够优美。
    跳出循环后，还需要做一次判断，以应对“0”，“1111”等这种需要最高位左边再加一个1的情况。

执行用时 :20 ms, 在所有 Python 提交中击败了73.68% 的用户
内存消耗 :12.8 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    
    def fast(self, num):
        newstr = bin(num)[2:]
        i = 0
        for char in newstr:
            if char == "1":
                i = i + 1
        if i == len(newstr):
            return True
        else:
            return False


    def reverseBits(self, num):
        #最笨的办法
        #先判断是不是全都是1111111
        if self.fast(num):
            result = len(bin(num)[2:]) + 1
            return result 
        #再用split函数对字符串进行分割
        newstr = bin(num)[2:]
        x = newstr.split("0")
        print(x)
        result = []
        for i in x:
            num = len(i)
            result.append(num)
        final = 0 
        for i in range(0, len(result)-1):
            temp_result = result[i] + result[i+1]
            if temp_result > final:
                final = temp_result
        final = final + 1
        return final
        
