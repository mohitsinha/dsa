from collections import deque
# DFS solution

def maxDepth(self, root ) -> int:
    def dfs(root):
        if not root: return 0

        return 1 + max(dfs(root.left), dfs(root.right))

    return dfs(root)



# BFS own soln

def maxDepth(root) -> int:
    if not root: return 0
    q = deque()

    q.append([root, 1])

    m = 1
    while q:
        pop = q.popleft()

        m = max(m, pop[1])

        if pop[0].left:
            q.append([pop[0].left, 1 + pop[1]])

        if pop[0].right:
            q.append([pop[0].right, 1 + pop[1]])

    return m


# https://www.youtube.com/watch?v=hTM3phVI6YQ&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=22
# different code
def maxDepth(self, root) -> int:

    if not root: return 0

    q = deque()

    q.append(root)

    level = 0
    while q:

        for i in range(len(q)):

            pop = q.popleft()

            if pop.left:
                q.append(pop.left)

            if pop.right:
                q.append(pop.right)

        level += 1

        return level


# Iterative DFS using stack

def maxDepth(self, root) -> int:

    if not root: return 0

    s = []

    s.append([root, 1])
    m = 1
    while s:
        node, depth = s.pop()
        m = max(m, depth)
        depth
        if node.left:
            s.append([node.left, 1 + depth])

        if node.right:
            s.append([node.right, 1 + depth])

    return m
