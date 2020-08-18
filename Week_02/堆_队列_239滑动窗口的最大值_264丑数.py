# coding:utf-8

# 239滑动窗口的最大值
class Solution:
    # solution1-暴力法，获取每个窗口中的最大值，返回即可
    # 窗口大小为k，待遍历序列中元素个数为n，则有n-k+1个窗口，每个窗口获取其中最大的数即可
    # 时间复杂度 (n-k+1)*取k个元素序列最大值的复杂度 = O(nk)
    # todo:超时
    def maxSlidingWindow_orgin(self, nums, k):
        n = len(nums)
        res = []
        if n*k ==0:
            return res
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res

    # solution2-优先队列 todo:待完成
    # 时间复杂度O(nlogk)，logk-插入1个元素logk+删除指定元素logk

    # solution3-单调双端队列，借助1个k个值的单调队列处理滑动窗口中的k个值
    # 目标是获取窗口中的最大值，单调队列的话，左端就是最大值，每次滑动直接取最左端元素就好
    # 每次滑动操作等价于，队列左端元素出去，右端追加1个元素
    # 每次增删元素后，我们需要保证队列的单调性，也就是最大值要到最左边（逐个对比将小元素左端出队就好）
    # ！每次出左端元素的时候需要判断下该元素是不是当前要加入的元素前n-k+1位个元素，因为保证队列单调性的过程中可能已经出队了，那么就不需要删除了
    # 单调双端队列的特点是：双端都可增删O(1)，单调递减保证左边的元素是单调队列中的最大值
    # 时间复杂度
    # 处理过程：初始化结果集/单调队列，塞k-1个值到单调队列中，遍历nums[k-1:],每次滑动调整单调队列，然后将单调队列的左值入到结果集中
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        # 初始化结果集/单调队列
        res, dq = [], MonotoneDeque()
        # 遍历nums
        for i in range(n):
            if i <k-1:  # 塞k-1个值到单调队列中
                dq.push(nums[i])
            else:  # 遍历nums[k-1:]
                dq.push(nums[i])  # 第一次加入该元素后窗口中有k个值
                res.append(dq.max())
                pre_k_item = nums[i - k + 1]
                dq.pop(pre_k_item)
        return res
# 单调双端队列类
class MonotoneDeque:
    def __init__(self):
        self.deque = []
    def push(self, item):
        # 尾端插入元素不断与前面的元素对比
        while self.deque and self.deque[-1] < item:
            self.deque.pop()
        self.deque.append(item)
    def max(self):
        if self.deque:
            return self.deque[0]
    def pop(self, n):
        if self.deque and self.deque[0] ==n:
            self.deque.pop(0)

# 264 丑数
# todo:需要消化一下，且耗时比较厉害，需要取优化
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]