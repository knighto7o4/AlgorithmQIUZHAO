# week04（0803-0809） 学习笔记
##  tips
- week4
1. 递归树理解处理过程
2. 动态规划~动态递推，将复杂问题分解为简单的子问题
=分治+最优子结构（每次处理子问题时通过比较和淘汰只保留最优状态）
3. 暴力递归/带备忘录的递归算法（自顶向下），带dp_table的动态规划（自底向上）
动态规划一般都脱离了递归，而是由循环迭代完成计算。
动态规划从最小的最底的最简单的情况下的问题逐渐向上推，直到想要的答案，也就是递推
所谓状态转移方程=递推公式=DP方程
4. 经验之说：
用空间换时间的思路，是降低时间复杂度的不二法门

5.labuladong的动态规划模板
base_case，最小的最底层的最基础的最简单的情况下的问题，比如路径统计时，离end最近的只有1种走法的情况就是base_case
状态，会发生变量的量（被动），按覃超的说法中间状态需要存储下来，因为要用于递推下一步 
选择，会导致状态变化的行为
dp函数/dp_table的含义， 




##  思考
- week4
1. 一周没有学习
动态规划+工作繁忙+周六有事-》敬而远之+毫无进展
痛苦的周日+海量的作业-》焦虑+专注力下降
想想起码要做的是：视频+6个题（0.5*6=3h）->开始吧
2. 动态规划 vs 递归



## 训练题表

|周序号| 题号 |题源| 训练点 | 训练次数  |最近训练时间|
|---| --------   |------ | ----- | ----  |----|
|week4|[.斐波那契数列]()|week04_1|DP|-|0809|
|week3|[367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)|week03_3_1|分治|-|0802|
|week3|[69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)|week03_3_1|分治|-|0802|
|week3|[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)|week03_2_1|贪心|-|0802|
|week3|[74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)|week03_2_1|贪心|-|0802|
|week3|[153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)|week03_2_1|贪心|-|0802|
|week3|[874. 模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/description/)|week03_2_1|贪心|-|0802|
|week3|[45. 跳跃游戏Ⅱ](https://leetcode-cn.com/problems/jump-game-ii/)|week03_2_1|贪心|-|0802|
|week3|[55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)|week03_2_1|贪心|-|0802|
|week3|[122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)|week03_2_1|贪心|-|0802|
|week3|[860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)|week03_2_1|贪心|-|0802|
|week3|[455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)|week03_2_1|贪心|2|0802|
|week3|[322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)|week03_2_1|贪心|-|0802|
|week3|[169. 多数元素]()|week03_1_3|分治|2|0728|
|week3|[51.N皇后](https://leetcode-cn.com/problems/n-queens/)|week03_1_3|回溯|2|0728|
|week3|[46.全排列](https://leetcode-cn.com/problems/permutations/)|week03_1_3|回溯|2|0728|
|week3|[17.电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)|week03_1_3|回溯|2|0728|
|week3|[79.子集](https://leetcode-cn.com/problems/subsets/)|week03_1_2|递归，位运算，回溯|2|0728|
|week3|[50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)|week03_1_2|分治|2|0727|
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
