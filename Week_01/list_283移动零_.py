# coding:utf-8

# 283.移动零
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 将所有非零的元素移动到前面去
        j =0  # 非零元素的新位置的起始位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]  # 将当前非零值移动到新的位置去
                if i != j:
                    nums[i] = 0
                j += 1  # j指向下一个位置，等待下一个非零值

# 42.接雨水


# 70.爬楼梯