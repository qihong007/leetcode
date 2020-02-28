'''
此题选自面试题
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Example 1:

Input: s = "leetcode"
Output: false

Example 2:

Input: s = "abc"
Output: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def isUnique(self, astr):
        '''
        for i in range(0, len(astr)-1):
            for j in range(i+1, len(astr)):

                if astr[i] == astr[j]:
                    return False

        return True
///该方法时间复杂度太高
