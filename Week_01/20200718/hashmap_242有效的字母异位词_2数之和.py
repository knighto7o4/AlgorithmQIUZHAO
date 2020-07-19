# coding:utf-8
import collections
# 242.有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1.clarification 大小写是否敏感等，该问题等价于：2个字符串中字符及出现次数相同
        # 2.possible solutions->optimal(time & space)
        # solution_1:分别sort然后对比排序后的结果，相等则是。 O(n2)
        # return sorted(s) == sorted(t)
        # solution_2:先统计s的字符词频c_counts,O(n)，再遍历t（O(n)）在c_counts中查找(O(1))，对应的字符值-1，最后c_counts值都为0则是
        c_counts = collections.defaultdict(int)
        for i in s:
            c_counts[i] += 1
        for j in t:
            c_counts[j] -= 1
        return not any(c_counts.values())
        # solution_3:


# 49.有效的字母异位词分组
import collections
class Solution:
    def groupAnagrams(self, strs):
        # solution1:遍历字符串O(n)，每个字符串排序(k*O(logk))后的结果作为hashmap的键，最后输出hashmap的值即可 O(nk*logk)
        # sorted_strs = collections.defaultdict(list)
        # for s in strs:
        #     sorted_s = str(sorted(s))
        #     sorted_strs[sorted_s].append(s)
        # return list(sorted_strs.values())
        # solution2: hashmap的键设置为：每个字符串在26位字符数组中各位字符的统计tuple
        # 时间复杂度O(nk)
        words_map = collections.defaultdict(list)
        for s in strs:
            init_array = [0]*26
            for c in s:
                init_array[ord(c)-ord('a')] += 1
            words_map[tuple(init_array)].append(s)
        return list(words_map.values())

# 299.猜数字游戏
import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 1.declarification 对比2个数字型字符串，
        # 2. solution1: 用hashmap的话，secret/guess分别构建1个字符和位置的map O(n)，构建过程中对比值，相同则A+1，然后求2个映射中每个字符统计中的最小值为in， B = in-A O(n)
        # 构建secret的字符位置映射
        s_indexs = collections.defaultdict(list)
        g_indexs = collections.defaultdict(list)
        a_count, in_count = 0, 0
        for i in range(len(secret)):
            s_indexs[secret[i]].append(i)
            g_indexs[guess[i]].append(i)
            a_count += secret[i] == guess[i]
        for k, v in s_indexs.items():
            in_count += min(len(v), len(g_indexs.get(k, [])))
        return str(a_count) + 'A' + str(in_count - a_count) + 'B'

# 1.两数之和
class Solution:
    def twoSum(self, nums, target):
        num_index = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            index = num_index.get(target-nums[i], None)
            # 数组中找到了值为target-num的元素，保证同1元素没有使用2遍
            if index and index != i :
                return [i, index]
        return None



# 15.3数之和



# 4数之和
