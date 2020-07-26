# coding:utf-8

"""
heapq模块
heapify(l)原地转化列表l为小顶堆
heappushpop(l, item) 比heappush()+heappop()高效；
heapreplace(l, item) 比heappop()+heappush()高效；
heapq.merge([],[])可合并几个有序列表，返回generator
nlargest(n, iterable, key=None),~sorted(iterable, key=key, reverse=True)[:n]
nsmallest(n, iterable, key=None)~sorted(iterable, key=key)[:n]
"""

# 前k个高频元素
import collections
class Solution:
    # solution1:统计各数字出现的次数，按次数排序，然后输出前k个次数对应的数字
    def topKFrequent(self, nums, k):
        num_count = collections.Counter(nums)
        sorted_list =  sorted(num_count.items(), key=lambda item:item[1], reverse=True)[:k]
        res = [k for k,v in sorted_list]
        return res

# 最小的k个数
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # solution1:排序，然后输出前k项
    # def getLeastNumbers(self, arr, k):
    #     return sorted(arr)[:k]

    # solution2: 调用系统的堆方法，选取k个元素，将其负值构建堆
    # 然后遍历arr中剩余的元素item，与堆顶的负值做对比，如果小于堆顶元素的负值则heappop堆顶，然后heappush该item的负值
    # 时间复杂度=建堆(k个元素的插入k*logk)+(n-k)*弹出栈顶O(1)
    def getLeastNumbers(self, arr, k):
        res = []
        if k <1:
            return res
        # heapify构建的是小顶堆，因此取arr的k个元素的负值构建小顶堆，堆顶的负值即为最大值
        heap = [-i for i in arr[:k]]
        heapq.heapify(heap)
        # 遍历剩余元素，更新堆
        for item in arr[k:]:
            largest_one = heapq.heappop(heap)
            new_one = 0-item if item < 0-largest_one else largest_one
            heapq.heappush(heap, new_one)
        # 转化堆中元素，然后输出
        res = [-i for i in heap]
        return res

    # solution3:直接建堆，然后k次弹出堆元素
    # 时间复杂度O(nlogn)=建堆n个元素的插入n*logn+k*弹出元素 todo:?
    def getLeastNumbers(self, arr, k):
        res = []
        heapq.heapify(arr)
        while k > 0:
            res.append(heapq.heappop(arr))
            k -= 1
        return res

    # solution4: 自己构建堆，todo:待实现

    # solution5:快排的思想， todo:带实现
