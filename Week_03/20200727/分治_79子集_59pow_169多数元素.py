# coding:utf-8

# 79.子集
'''

'''
print()

# 59.pow
# solution1-子集最多有n位元素，对应nums中各num，每个num都可能在/不在，因此有2**n种结果
# 构建每个可能：i和子集的关系？->每个i都可以表示为n为2进制
# 和nums的小标按位与之后取非0索引对应值就可以得到1个子集结果
# 按位与怎么实现？bin(a&b)两个数与之后的二进制表示（字符串）
# 遍历nums，将nums的下标与n位掩码进行按位与。比如掩码是101，那么temp就是{1,3},掩码是100，那么temp就是{3},掩码是111，那么temp就是{1,2,3}
def subsets(self, nums):
    res = []
    n = len(nums)
    nth_bit = 1 << n
    for i in range(2 ** n):
        # 将 i转化为3位的二进制字符串，左边以0填充
        bitmask = bin(i | nth_bit)[3:]  # 为啥取后3位？
        subset = [nums[j] for j in range(n) if bitmask[j] == '1']
        res.append(subset)
    return res

# 枚举所有可能性，每增加1个元素，之前的幂集就都加1个元素
# solution2-迭代-时间复杂度-O(n*(2**n))
# def subsets(self, nums):
#     res = [[]]
#     for i in range(len(nums)):
#         for subres in res[:]:
#             res.append(subres + [nums[i]])
#     return res
# solution3-回溯，递归 todo:需要继续去理解
# def subsets(self, nums):
#     res = []
#     # 递归终止条件
#     if not nums:
#         return res
#     n = len(nums)
#     #当前层处理
#     def helper(idx, tmp_list):
#         res.append(tmp_list)
#         for i in range(idx, n):
#             helper(i+1, tmp_list+[nums[i]])
#     #调用递归
#     helper(0, [])
#     return res
# solution4-DFS
# 集合中共n个元素，1个元素，有2种选择，接下来1位又有2种选择，直到最后1个元素，
# 最终的选择就是子集之一，构成了1个满二叉树，到叶子结点的所有路径，构成了所有子集
# 有前中后序不同写法, todo:待实现
# def subsets(self, nums):

# solution5-回溯
def subsets5(nums):
    def backtrace(subset, nums, start):
        # 结束条件
        res.append(subset[:])
        # 当前层处理
        for i in range(start, n):
            # 做选择，并更新状态集和可选列表，num就是当次的选择
            # 同时，num之前的元素已经遍历过，下次做横向选择的时候应该从num之后开始选择，否则已经选过的元素会被重复尝试
            # 不只是remove,应该时切片取
            subset.append(nums[i])
            # 下钻
            backtrace(subset, nums, i + 1)  # 此处当前的选择之后的选择作为下一次的选项列表
            # 撤销选择，继续横向尝试
            subset.pop()
    res = []
    n = len(nums)
    backtrace([], nums, 0)
    return res
print('subset5:', subsets5([1,2,3]))

# 169.多数元素, todo:
'''
'''
print()