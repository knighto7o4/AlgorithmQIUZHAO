# week01（0713-0719） 学习笔记
##  tips
1. 五毒神掌
  1)5-10分钟：读题&思考
  2)有思路->切题四件套；没思路->看题解
  3)第一遍 理解，背诵，熟练->机械记忆 
  4)第二遍：默写
  5)第三遍：1天后，重复做（新+旧这个太难了，就努力吧）
  6)第四遍：一周后继续练习
  7)面试前恢复性训练（笔记的重要性）
2. 切题四件套（单题做法）
  1)明确题意。输入限制（大小写？字符类型？边界？）/输出要求？
  2)罗列可能解法->最优解（时/空复杂度最优）
  3)编码
  4)测试
3. 自顶向下编程
  1)确定主干逻辑
  2)研究实现细节
4. CMU15121
5. 并不存在完美的数据结构，否则也不需要数组和链表并存了。（言之有理啊）
6. 有序数组，二分查找，快
7. 有序链表加速查询->跳表
8. 一维数据结构，加速法之一：升维变二维
9. 懵逼了怎么办？ 参见week01_1_2_爬楼梯懵逼解法
  1)能不能暴力？
  2)化繁为简，考虑基本情况
  3）递推，找最近*重复*子问题
10. 双指针，大部分时候在有序序列上应用
11. 队列实现栈（用2个队列），栈实现队列（用2个栈）
12. deque(double_ended_queue) = queue+stack
13. priority queue 插入O(1),取出O(logn)->按优先级取出->取最值
14. hash table工程抽象-> set, dict(map)
15. 常用数据结构的时间复杂度表

##  思考
1. 跳表需要再看看
2. linked-list应用 [LRU缓存算法](https://www.jianshu.com/p/b1ab4a170c3c) 
3. skip-list 应用 [redis](https://www.zhihu.com/question/20202931)
4. deque在python中的用法
见文件 dequeue_239滑动窗口.py
5. queue/priorityQueue在python中的实现原理？
ing...
*With a priority queue, the entries are kept sorted (using the heapq module) and the lowest valued entry is retrieved first.*
A typical pattern for entries is a tuple in the form: (priority_number, data)
6. hash map在python中的实现原理及接口使用？
ing...
7. 为什么用栈解决？什么样的问题可以用栈解决？
ing...
最近相关性（有一定距离的成对出现？）->栈
8. *python heapq/collections了解*
## 训练题表

| 题号 |题源| 训练点 | 训练次数  |最近训练时间|
| --------   |------ | ----- | ----  |----|
|146.LRU缓存机制|week01_1_1|double linked-list|-|-|
|283.移动零|week01_1_2/周作业|list|1|0720|
|42.接雨水|week01_1_3/week01_2_2/周作业|list|-|-|
|70.爬楼梯|week01_1_3|递归|-|-|
|15.三数之和|week01_1_4|数组/hash_table/双指针|-|-|
|206. 反转链表|week01_1_4|linked_list|-|-|
|24. 两两交换链表中的节点|week01_1_4|linked_list|-|-|
|141. 环形链表|week01_1_4|linked_list|-|-|
|142. 环形链表 II|week01_1_4|linked_list|-|-|
|25. K 个一组翻转链表|week01_1_4|linked_list|-|-|
|26. 删除排序数组中的重复项|week01_1_4/周作业|数组/双指针|||
|189. 旋转数组|week01_1_4|数组|-|-|
|21. 合并两个有序链表|week01_1_4/周作业|linked_list|-|-|
|88. 合并两个有序数组|week01_1_4/周作业|数组/双指针|-|-|
|66. 加一|week01_1_4/周作业|数组|-|-|
|20.有效的括号|week01_2_2|stack||0719|
|155.最小栈|week01_2_2|stack|-|-|
|84.柱状图中最大的矩形|week01_2_2|stack|-|-|
|239.滑动窗口最大值|week01_2_2|deque|||
|641.设计循环双端队列|week01_2_2/周作业|deque|||
| 242.有效的字母异位词|week01_3_2/周作业|hash_table|2|0718|
| 49.字母异位词分组|week01_3_2/周作业 |hash_table|2|0718|
| 299.猜数字游戏 |0718推荐每日一题|hash table|2|0718|
| 1.两数之和|week01_3_2/周作业 | hash_table | 2 |0718|
| 18.四数之和|题1关联 | hash_table/数组/双指针| - |-|
