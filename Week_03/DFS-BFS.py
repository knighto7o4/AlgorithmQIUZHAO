# coding:utf-8

# dfs递归写法
visited = set()
def dfs(node, visited):
    # 终止条件
    if node in visited:
        return
    visited.add(node)
    # 当前层处理
    for next_node in node.children:
        if not next_node in visited:
            dfs(next_node, visited)

# 非递归写法
def dfs(self, tree):
    if tree.root is None:
        return []
    visited, stack = (), [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes
        stack.push(nodes)

# 广度优先遍历，不用递归不用栈，用队列(数组和depue都可以实现)
def BFS(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generete_related_nodes(node)
        queue.push(nodes)