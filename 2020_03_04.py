'''
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"

Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation: 
The compressed string is "a1b2c2d1", which is longer than the original string.

执行用时：212 ms
内存消耗：14.4 MB

'''
class Solution(object):
    def compressString(self, S):
        if len(S) <= 1:
            return S
        s = S[0]
        num = 1
        for i in range(0, len(S)-1):
            s0 = S[i]
            s1 = S[i+1]
            if s0 == s1:
                num = num + 1
               
            else:
                s = s + str(num) + s1
                num = 1
                
            if i+1 == len(S)-1:
                s = s + str(num)  
            
        if len(S) > len(s):
            return s   
        return S
