def BFS():
    node=5
    edge=[[1,0],[0,3],[2,1],[3,1],[2,4]]
    graph={}
    start=0
    visited=[False for i in range(node)]
    for i in range(node):
        graph[i]=[]
    for i,j in edge:
        graph[i]+=[j]
        graph[j]+=[i]
    queue = []
    queue.append(start)
    visited[start] = True
    while queue:
        s = queue.pop(0)
        print(s)
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
