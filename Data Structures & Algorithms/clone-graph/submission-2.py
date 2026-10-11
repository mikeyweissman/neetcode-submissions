"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def bfs(self,node):
        while self.queue:
            for i in range(len(self.queue)):
                node = self.queue.popleft()
                if node not in self.nodes:
                    newNode = Node()
                    newNode.val = node.val
                    self.nodes[node] = newNode
                
                newNode = self.nodes[node]
                    
               

                for j in node.neighbors:
                    if j in self.nodes:
                        newNode.neighbors.append(self.nodes[j])
                        continue
                        
                    neighborNode = Node()
                    neighborNode.val = j.val
                    self.nodes[j] = neighborNode
                    newNode.neighbors.append(neighborNode)
                    self.queue.append(j)

                

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.queue = deque()
        self.nodes = {}
        if not node:
            return None
        
        else:

            self.queue.append(node)
            self.bfs(node)
        
        return self.nodes[node]





        