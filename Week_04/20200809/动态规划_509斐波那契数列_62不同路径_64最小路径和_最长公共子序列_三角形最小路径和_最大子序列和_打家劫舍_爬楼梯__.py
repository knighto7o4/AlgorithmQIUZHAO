# coding:utf-8

# 分治，回溯，递归，动态规划

# 递归模板
def recr(level, parm):
    # 终止条件
    if level>MAX_LEVEL:
        return
    # 处理当前层
    process(level, parm)
    # 进入下一层
    recur(level+1, updated(parm))
    # 恢复当前状态值

# 分治，将大问题分解成子问题，处理子问题再合并下
def divide_conquer(problem, param1, param2,):
    # 终止条件
    if problem is None:
        print_result
        return
    # 准备数据
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # 处理子问题
    subresult1 = divide_conquer(subproblems[0], p1, p2,)
    subresult2 = divide_conquer(subproblems[1], p1, p2, )
    subresult3 = divide_conquer(subproblems[2], p1, p2, )
    # 合并结果
    result = process_result(subresult1, subresult2, subresult3, )
    # 恢复当前状态




# 509.斐波那契数列
# 递归-简单易想的O(n*2)时间复杂度
def fib1(self, N: int) -> int:
    if N <2: # 0/1返回自身
        return N
    else:
        return self.fib(N-1)+self.fib(N-2)

# 递归-自顶向下-加缓存保存已经中间状态避免重复计算
def fib2(self, N, fibs={}) -> int:
    #  终止条件
    if N <= 1:
        return N
    if N > len(fibs)-1 :
        fibs[N] = self.fib(N-1, fibs) + self.fib(N-2, fibs)
    return  fibs[N]

# 动态规划-自底向上
def fib(self, N):
    dp_table = [0, 1]
    for i in range(2, N+1):
        dp_table.append(dp_table[i-1] + dp_table[i-2])
    return dp_table[N]

# 64.最小路径和
def minPathSum(grid) -> int:
    for i in range(len(grid)):  # 第i行，
        for j in range(len(grid[0])):  # 第j列
            # 第一行没有上值， 第一列没有左值
            up_value = grid[i-1][j] if i>0 else 0
            left_value = grid[i][j-1] if j>0 else 0
            if up_value and left_value:
                grid[i][j] += min(up_value, left_value)
            elif up_value:  # 非首行
                grid[i][j] += up_value
            elif left_value:
                grid[i][j] += left_value
    return grid[-1][-1]