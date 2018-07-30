node=9
edge=[[0,1],[1,2],[0,2],[1,5],[2,5],[2,6],[3,4],[3,6],[3,7],[4,6],[4,7],[5,6],[5,8],[6,7],[6,8],[2,3],[2,4]]
k=3
k_core_graph(node,edge, k)
def k_core_graph():
    def dfs(s):
        visited[s]=True
        for i in graph[s]:
            if degree[s]<k:
                degree[i]-=1
            if visited[i]==False:
                dfs(i)
        return degree[s]<k
    graph={}
    visited=[]
    degree=[]
    for i in range(node):
        graph[i]=[]
        visited+=[False]
    for i,j in edge:
        graph[i]+=[j]
        graph[j]+=[i]
    for i in range(node):
        degree+=[len(graph[i])]
    dfs(0)
    for i in range(node):
        if visited[i]==False:
            dfs(i)
    print(degree)
    for i in graph:
        s=''
        if degree[i]>=k:
            s+="[ "+str(i)+' ] ->'
            for j in sorted(graph[i]):
                if degree[j]>=k:
                    s+=' '+str(j)
            print(s)
    
