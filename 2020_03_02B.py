class Solution(object):
    def replaceSpaces(self, S, length):
        '''
        newstr = S[0:length]
        laststr = newstr.replace(" ", "%20")
        return laststr
        '''
        '''
        不用replace函数的话，可以复制一个新的字符串

        

        '''
        a = ""
        for i in range(0, length):
            a = a + S[i]
        b = ""
        for i in range(0, length):
            if a[i] == " ":
                b = b + "%20"
            else:
                b = b + a[i]
        return b
            
        """
        :type S: str
        :type length: int
        :rtype: str
        """
