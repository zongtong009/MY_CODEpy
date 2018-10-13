class Solution:
    def toRm(self, num):
        ones = ["", "I", "II", "III",
                     "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX",
                     "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC",
                         "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thounsands = ["", "M", "MM", "MMM"]

        sb = ''
        sb = sb+thounsands[num/1000] \
            + hundreds[(num % 1000)/100] \
            + tens[(num % 100)/10] \
            + ones[num % 10]
        return sb

'''
class Solution:
    def intToRoman(self, num):


        num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res=''
        for i in range(len(num_list)):
            while num>=num_list[i]:
                num-=num_list[i]
                res+=str_list[i]
        return res
            
'''
'''
class Solution:
    def intToRoman(self, num):

        q = num // 1000
        num = num - q * 1000
        b = num // 100
        num = num - b * 100
        s = num // 10
        num = num - s * 10
        g = num % 10

        ret = ""
        if q > 0:
            while q > 0:
                ret += "M"
                q -= 1
        if b > 0:
            if b == 9:
                ret += "CM"
            elif b >= 5:
                ret += "D"
                while b > 5:
                    ret += "C"
                    b -= 1
            elif b == 4:
                ret += "CD"
            else:
                while b > 0:
                    ret += "C"
                    b -= 1

        if s > 0:
            if s == 9:
                ret += "XC"
            elif s >= 5:
                ret += "L"
                while s > 5:
                    ret += "X"
                    s -= 1
            elif s == 4:
                ret += "XL"
            else:
                while s > 0:
                    ret += "X"
                    s -= 1

        if g > 0:
            if g == 9:
                ret += "IX"
            elif g >= 5:
                ret += "V"
                while g > 5:
                    ret += "I"
                    g -= 1
            elif g == 4:
                ret += "IV"
            else:
                while g > 0:
                    ret += "I"
                    g -= 1

        return ret
        '''