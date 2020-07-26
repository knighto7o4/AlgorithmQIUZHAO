# coding:utf-8

# 树的结点的类
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
二叉搜索树/有序二叉树/排序二叉树，是指一棵空树或者具有下列性质的二叉树：
左子树上所有结点的值均小于它的根节点的值；
右子树上所有结点的值均大于它的根结点的值；
以此类推：左/右子树也分别为二叉查找树
中序遍历：升序排列
"""

class Solution:

    # 二叉树中序：左根右
    # def inorderTraversal(self, root):
    #     # 递归版
    #     res = list()
    #     def travel(root, res):
    #         if root is None:
    #             return
    #         if root.left:
    #             travel(root.left, res)
    #         res.append(root.val)
    #         if root.right:
    #             travel(root.right, res)
    #     travel(root,res)
    #     return res

    # 迭代solution1
    # def inorderTraversal(self, root):
    #     stack, res, cur = [],[], root
    #     # 左子树都遍历完stack为空，存在右子树的话cur指向右子树仍需要遍历
    #     while stack or cur:
    #         # 遍历当前结点的左子树
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         # 左子树走到了尽头，弹出栈顶元素，为根节点
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         # if cur.right:  todo:加这句会超时，运行出错，why？
    #         cur = cur.right
    #     return res

    # 迭代solution2
    # def inorderTraversal(self, root):
    #     stack, rst = [root], []
    #     while stack:
    #         i = stack.pop()
    #         if isinstance(i, TreeNode):
    #             stack.extend([i.right, i.val, i.left])
    #         elif isinstance(i, int):
    #             rst.append(i)
    #     return rst

    # 迭代solution3，根节点遍历2次，第一次用来取左右节点然后子树的3个点压栈，第二次作为子树的根节点别处理
    def inorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            item = stack.pop()
            if item:
                if item !='root':
                    # 中序结果顺序左根右，入栈顺序右根左
                    stack.extend([item.right, item, 'root', item.left])
                else:
                    root_node = stack.pop()
                    res.append(root_node.val)
        return res

    # 二叉树前序遍历：根左右
    # solution1: 常规做法
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            # 弹出根节点,值入结果列表
            cur = stack.pop()
            res.append(cur.val)
            # 右结点先压栈后遍历
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
                    # solution2: 来自颜色标记法评论中的变形，类似于solution3
    # def preorderTraversal(self, root):
    #     stack, res = [root], []
    #     while stack:
    #         item = stack.pop()
    #         if isinstance(item, TreeNode):
    #             stack.extend([item.right, item.left, item.val])
    #         elif isinstance(item, int):
    #             res.append(item)
    #     return res

    # solution3：根节点会被遍历两次，第一次通过它获取左右结点，第二次进行作为当前子树的根的处理
    # def preorderTraversal(self, root: TreeNode):
    #     stack, res = [root], []
    #     while stack:
    #         cur = stack.pop()
    #         if cur:
    #             if cur != 'root':
    #                 stack.extend([cur.right, cur.left, cur, 'root'])
    #             else:
    #                 traveled_node = stack.pop()
    #                 res.append(traveled_node.val)
    #     return res

    # N叉树的后序遍历
    # solution1-迭代,过两遍根，第一遍用来取所再子树子节点然后压栈，第二遍对整个树进行处理
    def postorder(self, root: 'Node') -> List[int]:
        stack, res = [root], []
        while stack:
            item = stack.pop()
            if item:
                # 一棵子树各结点入栈
                if item != 'root':
                    # 入栈顺序：根，孩子们
                    stack.append(item)
                    stack.append('root')
                    # 此处倒序，保证子节点们的入栈顺序为从右到左
                    stack.extend(item.children[::-1])
                else:
                    root_node = stack.pop()
                    res.append(root_node.val)
        return res

    # solution2-迭代,颜色遍历法的变形，类两遍根法
    # def postorder(self, root):
    #     stack, res = [root], []
    #     while stack:
    #         item = stack.pop()
    #         if isinstance(item, Node):
    #             stack.append(item.val)
    #             stack.extend(item.children[::-1])
    #         elif isinstance(item, int):
    #             res.append(item)
    #     return res

    # solution3-递归:
    # def postorder(self, root):
    #     res = []
    #     if root:
    #         for item in root.children:
    #             res += self.postorder(item)
    #         res.append(root.val)
    #     return res

    # N叉树的前序遍历
    # 前序结果输出顺序：根，子结点们
    # solution1-迭代
    # def preorder(self, root: 'Node') -> List[int]:
    #     stack, res = [root], []
    #     while stack:
    #         item = stack.pop()
    #         if isinstance(item, Node):
    #             # 子树的结点压栈, 顺序为子节点们(从右到左)，根值
    #             stack.extend(item.children[::-1]+[item.val])
    #         elif isinstance(item, int):
    #             res.append(item)
    #     return res
    # solution2-递归
    def preorder(self, root):
        res = []
        if root:
            res.append(root.val)
            for child in root.children:
                res += self.preorder(child)
        return res

