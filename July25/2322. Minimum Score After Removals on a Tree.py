# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
#
# You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
#
# Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:
#
# Get the XOR of all the values of the nodes for each of the three components respectively.
# The difference between the largest XOR value and the smallest XOR value is the score of the pair.
# For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
# Return the minimum score of any possible pair of edge removals on the given tree.

class Solution:
    def minimumScore(_,N,E):
     n=len(N);g=[[]for _ in N]
     for u,v in E:g[u]+=[v];g[v]+=[u]
     s=[0]*n;d=[0]*n
     def D(u,p):
      s[u],d[u]=N[u],1<<u
      for v in g[u]:
       if v-p:D(v,u);s[u]^=s[v];d[u]|=d[v]
     D(0,-1)
     r,t=9e9,s[0]
     for i in range(1,n):
      for j in range(i+1,n):
       x,y=s[i],s[j]
       k=(y,x^y,t^x)if d[i]>>j&1 else(x,y^x,t^y)if d[j]>>i&1 else(x,y,t^x^y)
       r=min(r,max(k)-min(k))
     return r