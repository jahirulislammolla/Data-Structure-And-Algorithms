def DFS(visited,start):
        print(start)
        visited[start]=True
        for i in graph[start]:
            if not visited[i]:
                DFS(visited,i)
    n=5
    edge=[[4,0],[0,3],[2,1],[3,1],[2,4]]
    graph={}
    visited=[]
    start=0
    for i in range(n):
        graph[i]=[]
        visited.append(False)
    for i,j in edge:
        graph[i]+=[j]
        graph[j]+=[i]
    DFS(visited,start)
