# week01（0720-0726） 学习笔记
##  tips
- week2
1. 堆
	- 使用场景：找最大/最小值
	- 常见实现：二叉堆（基于完全二叉树，不是~~二叉搜素树~~），斐波那契堆（基于多叉树）
	- 时间复杂度：
建堆-插入n（元素个数）遍，nlogn
查找(最值)-O(1)
删除（堆顶元素）-O(logn)，删除堆顶将尾部元素移到堆顶后与左右子树对比再下移
插入-O(logn)或O(1)，元素加到尾部，然后与父元素对比逐步上移
	- 对比：
vs 排序后的数组，插入（伴随排序）-O(nlogn)，删除(头元素)-O(n) ——升维——》 堆（基于二叉树） 
2. heapq模块
``heapify(l)原地转化列表l为小顶堆
heappushpop(l, item) 比heappush()+heappop()高效；
heapreplace(l, item) 比heappop()+heappush()高效；
heapq.merge([],[])可合并几个有序列表，返回generator
nlargest(n, iterable, key=None),~sorted(iterable, key=key, reverse=True)[:n]
nsmallest(n, iterable, key=None)~sorted(iterable, key=key)[:n]
``
3. 本周最大的收获
来自周日下午Easley的分享，不要累计到一天去完成（深有体会），对自己多点包容心
4. 需要调整的点
    - 学习和做题分散到一周的时间去完成
    - 尽量参与到大家的讨论中，匹配大家的节奏
    - 再去试着，先完成题目，再**过遍数**，也就是五毒神掌的应用，不要恋战，不要苦思冥想

##  思考
- week2
1. 树的结点类和前中后序遍历方法
见 20200722
2. PriorityQueue~堆？
3. 最后一节的内容还没看，今天先把这周最后的1个视频过一遍吧，明早做下题
4. 下周任务貌似有点重，紧跟紧跟
## 训练题表

|周序号| 题号 |题源| 训练点 | 训练次数  |最近训练时间|
|---| --------   |------ | ----- | ----  |----|
|week2|[剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)|week02_2_2|堆(PriorityQueue)|1|0726|
|week2|[347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)|week02_2_2|堆（PriorityQueue）|3|0725|
|week2/week1|[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)|week02_2_2/week01_2_2|堆（PriorityQueue）, deque|2|0726|
|week2|[剑指offer40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)|week02_2_2|堆（PriorityQueue)|3|0725|
|week2|[94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)|week02_1_1|树|2|0724|
|week2|[144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)|week02_1_1|树|2|0724|
|week2|[590. N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)|week02_1_1|树|2|0724|
|week2|[589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)|week02_1_1|树|2|0724|
|week2|[429. N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)|week02_1_1|树|-|-|
|week1|146.LRU缓存机制|week01_1_1|double linked-list|-|-|
|week1|283.移动零|week01_1_2/周作业|list|1|0720|
|week1|42.接雨水|week01_1_3/week01_2_2/周作业|list|-|-|
|week1|70.爬楼梯|week01_1_3|递归|-|-|
|week1|15.三数之和|week01_1_4|数组/hash_table/双指针|-|-|
|week1|206. 反转链表|week01_1_4|linked_list|-|-|
|week1|24. 两两交换链表中的节点|week01_1_4|linked_list|-|-|
|week1|141. 环形链表|week01_1_4|linked_list|-|-|
|week1|142. 环形链表 II|week01_1_4|linked_list|-|-|
|week1|25. K 个一组翻转链表|week01_1_4|linked_list|-|-|
|week1|26. 删除排序数组中的重复项|week01_1_4/周作业|数组/双指针|||
|week1|189. 旋转数组|week01_1_4|数组|-|-|
|week1|21. 合并两个有序链表|week01_1_4/周作业|linked_list|-|-|
|week1|88. 合并两个有序数组|week01_1_4/周作业|数组/双指针|-|-|
|week1|66. 加一|week01_1_4/周作业|数组|-|-|
|week1|20.有效的括号|week01_2_2|stack||0719|
|week1|155.最小栈|week01_2_2|stack|-|-|
|week1|84.柱状图中最大的矩形|week01_2_2|stack|-|-|
|week1|239.滑动窗口最大值|week01_2_2|deque|||
|week1|641.设计循环双端队列|week01_2_2/周作业|deque|||
|week1| 242.有效的字母异位词|week01_3_2/周作业|hash_table|2|0718|
|week1| 49.字母异位词分组|week01_3_2/周作业 |hash_table|2|0718|
|week1| 299.猜数字游戏 |0718推荐每日一题|hash table|2|0718|
|week1| 1.两数之和|week01_3_2/周作业 | hash_table | 2 |0718|
|week1| 18.四数之和|题1关联 | hash_table/数组/双指针| - |-|
