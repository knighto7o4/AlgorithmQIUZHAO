# coding:utf-8

'''
应用前提：
1.单调性，即待查找序列是有序的
2.存在上下界，以进行二分
3.可以通过索引找到，二分按照索引来进行，因此需要通过索引能够找到值
'''

# 代码模板
def bin_search(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        mid  = (left+right)/2
        if array[mid] == target:
            break
            return target  # 中断或者返回
        elif array[mid] <target:
            left = mid+1
        else:
            right = mid-1

# 33.搜索旋转排序数组
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别
'''
def search(nums, target):
    # O(logn)~二分查找
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left)//2
        if target == nums[mid]:
            return mid
        if nums[left] <=nums[mid]: # 左侧单调递增
            if target >= nums[0] and target < nums[mid]:  # target位于左边有序区,左边界要是闭区间
                right = mid -1
            else:  # 在右边，left变换
                left = mid +1
        else:  # 右侧单调递增
            if target <= nums[right] and target > nums[mid]:  # 右边界要是闭区间
                left = mid +1
            else:
                right = mid - 1
    return -1

# 寻找旋转点, todo:有问题！再试吧
def search_rotation(nums):
    left, right = 0, len(nums) -1
    while left < right:
        mid = left + (right - left)//2
        if nums[left] <= nums[mid]:  # 左边有序，旋转点在右边
            left = mid +1
        else:  # 右边有序，旋转点在左边，right变换
            right = mid -1
    return left
print('search_rotation', search_rotation([4,5,6,7,0,1,2]))