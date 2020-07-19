# coding:utf-8

'''
1.为什么用栈解决？什么样的问题可以用栈解决？
最近相关性（有一定距离的成对出现？）->栈
'''

# 20.有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        # 构建左右括号映射，构建一个栈
        # 遍历输入字符串
        # 如果是左括号，入栈，如果是右括号，
        # 取栈顶元素，get该栈顶元素对应的右括号，对比当前右括号，不等则false
        # 遍历完成，判断是否栈空，空则有效
        # !空串有效
        stack = []
        lr_map = {'(':')','[':']','{':'}'}
        for c in s:
            if c in lr_map:
                stack.append(c)
            elif c in lr_map.values():
                # 右括号涉及取栈顶操作，先判断是否空栈
                if stack:
                    if lr_map.get(stack.pop(), None) !=c:
                        return False
                else:  # 栈已空，现在遇到的是右括号
                    return False
            else:  # 其他元素
                return False
        # 遍历结束，判断是否栈空，不空说明还有未匹配到的元素
        return stack==[]

# 155.最小栈


# 84.柱状图中最大的矩形，类似接雨水？


# 接雨水
#