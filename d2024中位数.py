class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        len1 = len(num)

        if len1 % 2 == 0:  # 能被2整除
            rtype = (num[int(len1/2)-1]+num[int(len1/2)])/2
        else:
            rtype = num[len1//2]  # 不能被2整除
        return rtype


def main():
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]

    rtype = s.findMedianSortedArrays(nums1, nums2)
    print(rtype)


if __name__ == '__main__':
    main()
