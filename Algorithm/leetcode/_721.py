from typing import List
from collections import defaultdict

class Solution:
    #Title: Accounts Merge
    #Approach: making graph and DFS
    #why?: The idea is like this. If you make a single account(list of emails
    #except name) into a graph, you eventually get merged graph since making
    #tree from a visited node would result on expanding the tree which also
    #means union of two accounts. When you done making tree, you can get answer
    #doing graph search.
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph, visited, ans = defaultdict(list), set(), []
        for account in accounts:
            for i in range(2, len(account)):
                graph[account[i]].append(account[i-1])
                graph[account[i-1]].append(account[i])

        def dfs(node):
            visited.add(node)
            result = [node]
            for child in graph[node]:
                if child not in visited:
                    result.extend(dfs(child))
            return result

        for account in accounts:
            if account[1] not in visited:
                ans.append([account[0]]+sorted(dfs(account[1])))
        return ans
