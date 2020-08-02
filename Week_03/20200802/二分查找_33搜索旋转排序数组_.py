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
            break or return target
        elif array[mid] <target:
            left = mid+1
        else:
            right = mid-1

#