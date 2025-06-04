#########################################################################
#-*- coding:utf-8 -*-
# File Name: hello.py
# Author: wayne
# mail: @163.com
# Created Time: 2015年08月17日 星期一 16时40分53秒
#########################################################################
#!/bin/python


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == nums[j]:
                    continue
                else:
                    return nums[i]
            
nums = [4,1,2,1,2]
So = Solution()
ret = So.singleNumber(nums)
print(ret)