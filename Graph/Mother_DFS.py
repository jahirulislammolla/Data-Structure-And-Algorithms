def Mother(visited,start):
        visited[start]=True
        for i in graph[start]:
            if not visited[i]:
                mother[i]+=[start]
                DFS(visited,i)
    n=5
    edge=[[4,0],[0,3],[2,1],[3,1],[2,4]]
    graph={}
    mother={}
    visited=[]
    start=0
    for i in range(n):
        graph[i]=[]
        mother[i]=[]
        visited.append(False)
    for i,j in edge:
        graph[i]+=[j]
        graph[j]+=[i]
    Mother(visited,start)
    print(mother)
