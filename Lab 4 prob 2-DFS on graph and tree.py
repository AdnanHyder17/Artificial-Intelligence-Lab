# Implement DFS on graph and tree.

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        if start not in visited:
            print(start)  # Process the node
            visited.add(start)
            for neighbor in self.graph.get(start, []):
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

class Tree(Graph):
    def __init__(self):
        # Initialize an empty adjacency list
        self.graph = {}
    
    def add_child(self, parent, child):
        if parent not in self.graph:
            self.graph[parent] = []
        if child not in self.graph:
            self.graph[child] = []
        self.graph[parent].append(child)

tree = Tree()
tree.add_child('A', 'B')
tree.add_child('A', 'C')
tree.add_child('B', 'D')
tree.add_child('B', 'E')

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')

print("DFS on Tree:")
tree.dfs('A')

print("\nDFS on Graph:")
graph.dfs('A')
