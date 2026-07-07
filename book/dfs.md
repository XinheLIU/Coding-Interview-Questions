# Depth-First Search(DFS)

```py
# recursive
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
        # already visited 
        return 

        visited.add(node) 

        # process current node here. 
        ...
        for next_node in node.children(): 
            if not next_node in visited: 
                dfs(next_node, visited)

# iterative

def DFS(self, tree): 

    if tree.root is None: 
        return [] 

    visited, stack = [], [tree.root]

    while stack: 
        node = stack.pop() 
        visited.add(node)

        process (node) 
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 

    # other processing work
```

- Applicable to most any problems
- storage cost low

## Applications

- [Flood Fill](https://en.wikipedia.org/wiki/Flood_fill)

Improvements

## Heuristic Seach

A\* algorithm: use Priority Queue

```py
def AstarSearch(graph, start, end):
    pq = collections.priority_queue() # Valuation function: key for performance
    pq.append([start]) 
    visited.add(start)

    while pq: 
        node = pq.pop() # can we add more intelligence here ?
        visited.add(node)

        process(node) 
        nodes = generate_related_nodes(node) 
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```

* key is [similarity measures](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)