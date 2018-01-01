# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        _len = len(rotateArray)
        left = 0
        right = _len - 1

        if rotateArray[0] < rotateArray[-1]:
            # 旋转0个元素的情况
            return rotateArray

        while left <= right:
            mid = int((left + right) >> 1)
            print(left,right,mid)
            if rotateArray[mid]<rotateArray[mid-1]:
                return rotateArray[mid]
            if rotateArray[mid] >= rotateArray[right]:
                # 说明在【mid，right】之间
                left = mid + 1
            else:
                # 说明在【left，mid】之间
                right = mid - 1
        return rotateArray[mid]

if __name__ == '__main__':
    s = Solution()
    result = s.minNumberInRotateArray([1,1,1,1,1])
    print(result)
