# coding:utf-8

"""191.位1的个数，返回给定的无符号的n的二进制表示中1的个数"""
# 懒蛋法，因为无符号，所以可用，有符号则不行，因为bin未将符号位包含在内
def hammingWeight1(n: int) -> int:
    return bin(n).count('1')
# n&(n-1)去掉最低位的1，直到n为0
def hammingWeight2(n:int):
    count = 0
    while n:
        count += 1
        n &= n-1
    return count
# n&1返回末位值，n>>1每次右移1位，判断当前末位是否为1
def hammingWeight(n):
    count = 0
    while n:
        count += n&1
        n = n>>1
    return count

""" 231.2的幂次， 判断1个数是否2的幂次"""
# 2的幂值的二进制表示中有且只有1个1，意味着n&(n-1)为0
# 懒蛋法，不行, 负数的情况不能处理
def isPowerOfTwo(n: int) -> bool:
    return n != 0 and n&(n-1)==0


"""338.比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。"""


# 也就是遍历小于num的所有值，返回每个值的二进制表示中1的个数
# 懒蛋法
def countBits1(self, num: int) -> List[int]:
    return [bin(i).count('1') for i in range(num + 1)]
# 递归
def countBits(self, num):
    # 子问题dp[i]表示i值中1的个数， dp[0]=0
    dp = [0 for i in range(num + 1)]
    # 递推公式,利用 i&(i-1)，消掉了1个1，于是加上1个1就是i中1的个数
    # dp[i] = dp[i&(i-1)] + 1
    # 自底向上
    for i in range(1, num + 1):  # 从1开始，0中包含0个
        dp[i] = dp[i & (i - 1)] + 1
    return dp

"""
190. 颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
"""
# 不断取余，对现有结果进位后加余数
def reverseBits1(self, n: int) -> int:
    res = 0
    # 已知32位，遍历即可
    for i in range(32):
        res = (res<<1) + (n&1)
        n = n>>1  # 或n>>1
    return res

# 通用，不限进制法
def reverseBits2(self, n, base=2):
    res = 0
    for i in range(32):
        yushu = n % base
        weizhi = res * base
        res = weizhi + yushu
        n = n // base
    return res
def reverseBits(self, n):
    return int(bin(n)[2:].zfill(32)[::-1],base=2)

"""
51.N皇后
返回可能的解法
"""


# 位运算，用一个int(有32位，可以用来求解32以内的N皇后，二进制表示中1表示可选0表示不可选)
# 来替代数组（queen_columns, xy_sum, xy_dif）表示已占用的位置
def solveNQueens(self, n):
    # 用数组记录占用位置的时候，可以通过已占用列的个数来获得当前行标，现在已占用列用1个数字表示，无法获取row，因为要记录path，就用path的长度来获取row
    def dfs(path, cols, xy_sum, xy_dif):
        row = len(path)
        # 终止条件
        if row == n:
            result.append(path[:])  # 切片复制，否则会随着path变化
            return
        # 当前行处理，从可选位置中选择1列，然后基于选择进入下一行
        # 可选位置
        init_row = (1 << n) - 1
        already_used = cols | xy_sum | xy_dif
        avalible_bits = init_row & ~(already_used)
        while avalible_bits:
            # 选择1列
            p = avalible_bits & -avalible_bits  # 获取最右边的也就是最低位的1
            path.append(p)  # 加入路径中
            avalible_bits = avalible_bits & (avalible_bits - 1)  # 更新avalible_bits
            dfs(path, cols | p, (xy_sum | p) << 1, (xy_dif | p) >> 1)
            # 撤销选择
            path.pop()
    result = []
    dfs([], 0, 0, 0)
    return [[bin(num)[2:].zfill(n).replace('0', '.').replace('1', 'Q') for num in one] for one in result]


"""
52.N皇后Ⅱ
返回可能的解法数
"""
def totalNQueens(n):
    def dfs(row, cols, xy_sum, xy_dif):
        nonlocal count  # 为啥result列表就不需要nonlocal？？
        if row >= n:
            count +=1
            return
        avalibles = ~(cols|xy_dif|xy_sum)&(1<<n)-1
        while avalibles:
            p = avalibles & -avalibles  # 获取最低位的1
            avalibles &= (avalibles-1)  # 将最低位的1置0
            dfs(row+1, cols|p, (xy_sum|p)<<1, (xy_dif|p)>>1)
    count = 0
    dfs(0, 0, 0, 0)
    return count