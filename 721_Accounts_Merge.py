"""
Name: Accounts Merge (#721)
URL: https://leetcode.com/problems/accounts-merge

Time Complexity: O(?) # TODO
Space Complexity: O(?) # TODO
"""

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return False

        rank_u = self.rank[u]
        rank_v = self.rank[v]

        if rank_u == rank_v:
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1
        elif rank_u > rank_v:
            self.parent[parent_v] = parent_u
        else:
            self.parent[parent_u] = parent_v

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email_to_accountIdx = {}
        
        for idx in range(len(accounts)):
            for email in accounts[idx][1:]:

                if email not in email_to_accountIdx:
                    email_to_accountIdx[email] = idx

                else:
                    prev_account_idx = email_to_accountIdx[email]

                    uf.union(idx, prev_account_idx)

        email_groups = {}

        for email in email_to_accountIdx.keys():
            account_idx = email_to_accountIdx[email]

            parent_acc_idx = uf.find(account_idx)

            if parent_acc_idx not in email_groups:
                email_groups[parent_acc_idx] = []

            email_groups[parent_acc_idx].append(email)

        result = []

        for acc_idx in email_groups.keys():
            emails = sorted(email_groups[acc_idx])
            account_name = accounts[acc_idx][0]
            
            result.append([account_name] + emails)
        
        return result