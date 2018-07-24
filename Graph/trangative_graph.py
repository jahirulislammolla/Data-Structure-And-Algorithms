def trangative_graph():
    def trangative(u,v):
        trangativ[u][v]=1
        for i in graph[v]:
            if trangativ[u][i]==0:
                trangative(u,i)
    edge=[[0,1],[1,2],[0,2],[2,0],[2,3]]
    graph={}
    n=4
    trangativ=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        graph[i]=[]
    for i,j in edge:
        graph[i]+=[j]
    for i in range(n):
        trangative(i,i)
    print(trangativ)
