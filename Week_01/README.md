# week01（0713-0719） 学习笔记
## 训练方法及tips
1. 五毒神掌
2. 切题四件套（单题做法）
1）明确题意。输入限制（大小写？字符类型？边界？）/输出要求？
2）罗列可能解法->最优解（时/空复杂度最优）
3）编码
4）测试
3. 自顶向下编程
1）确定主干逻辑
2）研究实现细节
4. 队列实现栈（用2个队列），栈实现队列（用2个栈）
5. deque(double_ended_queue) = queue+stack
6. priority queue 插入O(1),取出O(logn)->按优先级取出->取最值
7. hash table工程抽象-> set, dict(map)
8. 常用数据结构的时间复杂度表

## 思考
1. deque在python中的用法
见文件 dequeue_239滑动窗口.py
2. queue/priorityQueue在python中的实现原理？
ing...
*With a priority queue, the entries are kept sorted (using the heapq module) and the lowest valued entry is retrieved first.*
A typical pattern for entries is a tuple in the form: (priority_number, data)
3. hash map在python中的实现原理及接口使用？
ing...
4. 为什么用栈解决？什么样的问题可以用栈解决？
ing...
最近相关性（有一定距离的成对出现？）->栈
5. *python heapq/collections了解*

## 训练题表
| 题号 |题源| 训练点 | 训练次数  |最近训练时间|
| --------   | | -----:  | :----:  |----|
| 242.有效的字母异位词|week01_3_2/周作业 | hash_table  |   2     |0718|
| 49.字母异位词分组|week01_3_2/周作业 | hash_table  |   2     |0718|
| 299.猜数字游戏 |0718推荐每日一题| hash table  |  2    |  0718  |
| 1.两数之和|week01_3_2/周作业 | hash_table  |   2     |0718|
| 15.三数之和|题1关联 | hash_table/？数组/？双指针| -     |-|
| 18.四数之和|题1关联 | hash_table/？数组/？双指针| -     |-|
|20.有效的括号|week01_2_2|stack||||
|155.最小栈|week01_2_2|stack||||
|84.柱状图中最大的矩形|week01_2_2|stack||||
|239.滑动窗口最大值|week01_2_2|deque||||
|设计循环双端队列|week01_2_2/周作业|deque||||
|接雨水|week01_2_2/周作业|stack||||
|删除排序数组中的重复项|/周作业|||||
|旋转数组|/周作业|||||
|合并两个有序链表|/周作业|||||
|合并两个有序数组|/周作业|||||
|移动零|/周作业|||||
|加一|/周作业|||||
