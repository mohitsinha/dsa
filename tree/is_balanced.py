# https://leetcode.com/problems/balanced-binary-tree/submissions/

class Solution:

    def isBalanced(self, root) -> bool:

        def height(root):
            if not root: return 0

            return 1 + max(height(root.left), height(root.right))

        if not root: return True
        l, r = height(root.left), height(root.right)

        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # https: // www.youtube.com / watch?v = QfJsau0ItOY & list = PLot - Xpze53ldg4pN6PfzoJY7KsKcxF1jg
    def solutionFaster(self, root):

        def dfs(root):
            if not root: return [True, 0]

            l, r = dfs(root.left), dfs(root.right)

            return [abs(l[1] - r[1]) <= 1 and l[0] and r[0], 1 + max(l[1], r[1])]

        return dfs(root)[0]


