from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Title: House Robber III
    #Approach: DP
    #Explanation: It's the harder version of House Robber Problem. Now we
    #have to search through binary tree. When you solve DP problems, defining
    #subproblem is all. In this problem, the max amount of money on random
    #node is the subproblem. I tried two approachs. First, you focus on saving
    #calculated results. Im going to define max amoun of money on node x
    #f(x). f(x) is expanded to max(x.val+f(x.grandchilds), f(x.childs)).
    #So you keep these three generation of nodes as a window, keep going up
    #from bottom of the tree by dfs. You need to do just dfs, which returns
    #nothing but updates DP List. The second approach is space optimized 
    #version. if in dfs function it returns it's current childs and grandchids,
    #there are all components to calc f(x) so the need of extra space disappear
    #s. In this version, you return a pair, f(x.childs), x,val+f(x.grandchilds)
    #. You just need to set return value of leef node to (0,0) and this will
    #work. 
    def rob(self, root: Optional[TreeNode], index=1) -> int:
        dp = defaultdict(int)
        def dfs(root, index):
            if not root: return
            dfs(root.left, index*2)
            dfs(root.right, index*2+1)
            below = dp[index*2]+dp[index*2+1]
            below_below = 0
            below_below += dp[index*2*2]+dp[index*2*2+1]
            below_below += dp[(index*2+1)*2]+dp[(index*2+1)*2+1]
            dp[index] = max(root.val+below_below, below)
            return
        dfs(root, 1)
        return dp[1]

    def rob_optimized(self, root):
        def dfs(root):
            if not root: return (0,0)
            left = dfs(root.left)
            right = dfs(root.right)
            return (max(left)+max(right), root.val+left[0]+right[0])
        return max(dfs(root))
