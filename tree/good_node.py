# https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/

class Solution:
    def goodNodes(self, root) -> int:

        def good(root, m):
            if not root: return 0

            l = r = 0
            if root.left:
                if root.left.val >= m:
                    l = 1 + good(root.left, root.left.val)
                else:
                    l = good(root.left, m)

            if root.right:
                if root.right.val >= m:
                    r = 1 + good(root.right, root.right.val)
                else:
                    r = good(root.right, m)

            return l + r

        return 1 + good(root, root.val)




    # https://www.youtube.com/watch?v=7cp5imvDzl4&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=2
    
    def goodNodesBetter(self, root) -> int:

        def dfs(root, m):

            if not root: return 0

            res = 0

            if root.val >= m:
                res = 1
                m = root.val

            res += dfs(root.left, m)
            res += dfs(root.right, m)

            return res

        return dfs(root, root.val)


