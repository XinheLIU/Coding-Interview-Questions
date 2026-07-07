# Breath-First Search\(BFS\)


Search on a graph

```py
def BFS(graph, start, end):

    queue = [] 
    queue.append([start]) 
    visited.add(start)

    while queue: 
        node = queue.pop() 
        visited.add(node)

        process(node) 
        nodes = generate_related_nodes(node) 
        queue.push(nodes)

    # other processing work
```

- Complete: can guarantee the solution to be found
- Storage cost high

Imprmprovements

## Double-direction BFS\(DBFS\) : expand from start point and end point

  ```py
  def BFS(graph, start, end):
      front, back = [start],[end]
      visited.add(start)

      while front and back: 
          # choose the short one to sarch
          queue = front if len(front) < back else back

          node = queue.pop() 
          visited.add(node)

          process(node) 
          nodes = generate_related_nodes(node) 
          queue.push(nodes)
  ```