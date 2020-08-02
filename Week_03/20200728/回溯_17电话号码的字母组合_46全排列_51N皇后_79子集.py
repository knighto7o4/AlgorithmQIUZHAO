# coding:utf-8

'''
回溯本质：遍历递归树
关键点：路径（已做出的选择），可选列表（但钱可以做的选择），结束条件（到达决策树的底层，无法再做选择的条件）

每一次方法的目的是输出1个结果，每个结果是有多次选择构成的，一个结果中的多次选择是有先后的，当前的选择可能会影响下一次可选的项，必然会改变正在构建的结果（可以说是1个状态集）

每次调用backtrace，
首先要检查当前的状态集是不是已经可以加到结果集了，所谓的'结束条件'指的是当前结果对应的纵向的选择已经都做完了，没有需要再下钻的层了，这个通常通过对1个结果的约束来判断
然后呢，当前层（横向）是有多个选择的（否则也不需要进行回溯了，回溯的目的是回到上一次做选择的时候，试下别的可能），
    从中选择1个，这个选择会产生2个纵向的影响，1.下一层的可选项可能会变化，2.正在构建的结果增加了1个内容，
    带着这2个变化后的内容和标识下一层的变量（有时通过前面2个变化了的内容隐形的替代）进入下一层，
    backtrace可以理解为我们进入1层的入口，带着即将进入层的内容，然后下一层结束的时候，也就是backtrace执行完
    返回到当前层，继续横向的选择（for choice in choices）,要继续就要把变更过的内容复原，有些情况（多层公用1个可选列表）下这个变更可以通过不改变当前层的内容实现，就是把要传递给下一层的内容直接拉两个变量指向拷贝就好，而不对当前的可选列表和状态集直接变化

所以回溯可以理解为是2个方向上的选择，每个横向的选择可以进行1次纵向的推进。
1个可能的结果就是纵向的各层1次选择的组合
'''

# *回溯代码框架
res = []
def backtrace(one_path, avalible_chooses):
    if '满足结束条件':
        res.append(one_path)
        return
    for choice in avalible_chooses:
        # 1种实现
        # 做选择
        avalible_chooses.pop(choice)
        one_path += choice
        # 对新的路径和可选列表继续调用
        backtrace(one_path, avalible_chooses)
        # 撤销选择，也就是遍历时的回退到上一层，为新的选择做准备
        one_path.pop()
        avalible_chooses += choice

        # 另1种实现：适用于多层不共用选择列表的情况，不改变当前层的信息（可选列表/状态集，把变更后的内容副本直接赋给新的变量，传给下一层）
        new_avalible_chooses = avalible_chooses.pop(choice)
        new_one_path = one_path + choice
        # 对新的路径和可选列表继续调用
        backtrace(new_one_path, new_avalible_chooses)

# 17.电话号码的字母组合
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 示例:
 输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
 Related Topics 字符串 回溯算法
'''
def letterCombinations(digits):
    num_chars = {'2': 'abc', '3': 'def', '4': 'ghi',
                 '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # 1个组合就是1个解，终止条件定为len(one_str)==len(digits)
    def backtrace(one_str, digit_index):  # 路径就是组合的字符串，可选列表就是通过当前数字（这个数字随着遍历逐渐后移）获得的对应字符
        # 终止条件：转化后字符串长度==待转化字符长度
        if len(one_str) == n:
            res.append(one_str)
            return
        # 遍历可选列表
        for char in num_chars[digits[digit_index]]:
            # 做选择,准备下一层要用到的 状态集和可选列表
            new_one_str = one_str + char
            # 下钻，带着加入当前选择的状态集和下一层的可选列表
            backtrace(new_one_str, digit_index+1)
            # 撤销选择，没有改变当前层的内容，就不需要去撤销，但是为什么模板会把这个撤销作为必选？为了更好的通用性？
            # one_str = one_str[:-1]
    res, n = [], len(digits)
    if digits:
        backtrace('', 0)  # 从第一个数字字符开始，查找每个字符的可选列表
    return res
print('--letterCombinations:', len(letterCombinations('345')),letterCombinations('345') )

# 46.全排列
'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
 示例:
 输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
] 
Related Topics 回溯算法
'''
def permute(nums):
    # 每个结果有3个元素，可选列表逐渐缩小
    def backtrace(subset, choices):
        # 终止条件
        if len(subset) == n:
            res.append(subset[:])  # 为了避免subset变化影响结果，将拷贝加入结果集
            return
        # 遍历可选条件
        for choice in choices:
            # 做选择
            subset.append(choice)
            choices.remove(choice)  # 从选择种去掉choice元素
            # 下钻
            backtrace(subset, choices)
            # 撤销选择
            subset.pop()
            choices.insert(0, choice)  # 将choice加回之前的位置

    res, n = [], len(nums)
    if not nums:
        return res
    backtrace([], nums)
    return res
print('--permute:',permute([1,2,3]))

# 51.N皇后
'''
n*n的棋盘，放置n个皇后，皇后不能在同x同y，正负45°2条线上
问所有的可能性，知道每行皇后的位置就算是拿到初步结果了，然后再根据输出要求转化即可
'''
def solveNQueens(n):
    def backtrace(row_idx, n, col_idx_list):  # 传入层数/可选内容(当前场景是列的可选范围)/状态集
        # 结束条件，最后一行的row_num是n-1，row_num==n时已经超出棋盘了，也就是纵向已经走完了
        if row_idx == n:
            final_result.append(col_idx_list[:])
            return
        # 当前层处理
        for col_idx in range(n):
            # 做选择，col_idx就是当次遍历的选择
            # 但需要判断下，这选择是不是满足条件
            # 有时候选择列表不好更新，我们借助其他对象来约束可选范围，有同样的效果
            if col_idx in cols or col_idx+row_idx in pie or col_idx-row_idx in na:
                continue
            col_idx_list.append(col_idx)
            cols.add(col_idx)
            pie.add(col_idx+row_idx)
            na.add(col_idx-row_idx)
            backtrace(row_idx+1, n, col_idx_list)
            # 撤销选择，准备横向的下一次尝试
            col_idx_list.pop()
            cols.remove(col_idx)
            pie.remove(col_idx+row_idx)
            na.remove(col_idx-row_idx)

    final_result, one_possibility = [], []
    cols, pie, na = set(), set(), set()
    backtrace(0, n, one_possibility)  # 从第0行开始，该层的列标可选范围为n，状态集为空
    return final_result
print('--solveNQueens:', solveNQueens(4))

# 169.多数元素

#
