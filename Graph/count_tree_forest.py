node=9
edge=[[0,1],[2,3],[0,2],[2,3],[4,5],[5,6],[7,8]]
count_tree_forest(node,edge)
def count_tree_forest(node,edge):
    def dfs(s):
        visited[s]=True
        for i in graph[s]:
            if visited[i]==False:
                dfs(i)
        return 0
    graph={}
    visited=[]
    for i in range(node):
        graph[i]=[]
        visited+=[False]
    for i,j in edge:
        graph[i]+=[j]
        graph[j]+=[i]
    count=0  
    for i in range(node):
        if visited[i]==False:
            dfs(i)
            count+=1
    print(count)
