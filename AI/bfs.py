# bfs
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=[];
queue=[];
def bfs(visited,graph,start,goal):
    visited.append(start);
    queue.append(start);
    while queue:
        m=queue.pop(0);
        print(m);
        if(m==goal):
            print("goal node found");
            break;
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n);
                    queue.append(n);


print("BFS Traversal");
bfs(visited,graph,'A','E');