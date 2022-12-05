# Tanmay Deshpande- 332057

from queue import PriorityQueue

class BestFirst:

  def addedge(self, v1,v2,cost):
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))

  def best_first_search(self,src1, target,n):
    visited=[False]*n
    pq=PriorityQueue()
    pq.put((0,src1))
    visited[src1]=True

    while pq.empty()==False:
      u=pq.get()[1]
      print(u,end=" ")

      if u==target:
        break

      for v,c in graph[u]:
        if visited[v]==False:
          visited[v]=True
          pq.put((c,v))
    print()



bfs= BestFirst()
v=14
graph=[[] for i in range(v)]

# pq([cost,vertex])
# graph([v,cost])

# addedge(v1,v2,cost)
bfs.addedge(0, 1, 3);
bfs.addedge(0, 2, 6);
bfs.addedge(0, 3, 5);
bfs.addedge(1, 4, 9);
bfs.addedge(1, 5, 8);
bfs.addedge(2, 6, 12);
bfs.addedge(2, 7, 14);
bfs.addedge(3, 8, 7);
bfs.addedge(8, 9, 5);
bfs.addedge(8, 10, 6);
bfs.addedge(9, 11, 1);
bfs.addedge(9, 12, 10);
bfs.addedge(9, 13, 2);

print("Graph is:")
print(graph)

source = 0
target = int(input("Enter target:"))

print("Path is:")
bfs.best_first_search(source, target, v)