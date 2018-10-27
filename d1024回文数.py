class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0 or (x % 10 == 0 and x != 0)) :
            return False

        revertedNumber = 0
        while(x > revertedNumber) :
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10
        '''当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        // 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        // 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        '''
        return x == revertedNumber or x == revertedNumber/10

s=Solution()
f=s.isPalindrome(121)
print(f)






