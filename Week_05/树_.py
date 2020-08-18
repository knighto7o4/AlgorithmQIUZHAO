# coding:utf-8

# 结点类
class TreeNode:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None

# 树的遍历。前序，中序，后序
def preorder(root):
    if root:
        traverse_path.append(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        traverse_path.append(root.value)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        traverse_path.append(root.value)

# 二叉搜索树(有序二叉树/排序二叉树)-》左<根 & 根<右， 左右子树均是二叉搜索树（重复性！！！）
# 中序有序， 查询/插入的时间复杂度O(logn)
# 插入和查询的实现


# 树和链表没有本质上的区别，极端情况下二叉搜素树退化为链表
# -》树的深度增加，查询/插入效率下降
# -》保证左右子树平衡（高度平衡）， how？？？-》每一步删除/插入的时候都保证其平衡性，而非等到成为棍子再行动
# ->常见平衡树：2-3tree,AVLtree,B-tree, 红黑树
# 平衡因子=左子树高度-右子树高度=平衡树的平衡因子：{-1，0，1}， 所有叶子结点平衡因子为0
# 旋转保平衡：左旋，右旋，左右旋，右左旋
# 左右旋，右左旋的第一次旋转之后仍然满足搜索树的性质
# -》平衡树结点需要维护额外信息，调整次数频繁-》近似平衡二叉树，平衡因子为2也没关系，不需要每次都调整
# 红黑树，一种近似平衡二叉树，左右子树的高度差小于2倍， 特点
# 结点要么红要么黑；根黑；叶节点（空结点）黑；不能右相连接的红；任一结点到其每个叶子的所有路径包含相同个数的黑
# 从根节点到叶子结点，最长的可能路径不多于最短可能路径长度的2倍

# AVL vs. 红黑树
# 查找：AVL更快（严格平衡）
# 插入删除：红黑树更快（近似平衡不需要更多旋转操作）
# 内存占用：AVL多余红黑树（需要存储高度，平衡因子等额外信息）