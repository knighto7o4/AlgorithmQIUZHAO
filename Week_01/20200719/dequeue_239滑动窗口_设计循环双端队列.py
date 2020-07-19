# coding:utf-8

# 1.deque的用法
import collections
# deque的用法,默认从右端进行，左端的操作方法就是默认方法加left后缀
the_deque = collections.deque()
# append 尾插元素：从左向右插入元素到deque
# appendleft 头插元素：从右向左插入元素到deque
the_deque.append('a')
the_deque.append('b')
the_deque.append('c')
print(the_deque)
# 返回deque的左右首两端元素
left_head, right_head = the_deque[0], the_deque[-1]  # 返回左首元素
print('the_queue:{},\n left_head:{}, right_heaed:{}'.format(the_deque,left_head, right_head))
# pop:从右向左弹出deque元素
# popleft:从左向右弹出deque元素
while the_deque:
    print(the_deque.pop())
print('the_queue:{}', the_deque)

# 2.queue/priorityQueue实现原理分析


# 239滑动窗口最大值

# 设计循环双端队列

