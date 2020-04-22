 /**
 设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。

示例:

输入: a = 1, b = 1
输出: 2

 

提示：

    a, b 均可能是负数或 0
    结果不会溢出 32 位整数

 执行用时 :0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗 :36.3 MB, 在所有 Java 提交中击败了100.00%的用户
 */
class Solution {
    
    public int add(int a, int b) {
        while (b != 0) {
            int sum = (a ^ b);
            int carry = (a & b) << 1;
            a = sum;
            b = carry;
        }

        return a;
    }

}
