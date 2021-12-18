nums = list(map(int,input().split()))

from collections import deque
queue = deque() #큐를 이용할 떄 쓰는 라이브러리 

#dfs_algrithm
# def dfs(graph, v, visited):
#     visited[v] =True
#     print(v,end='')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

# graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# visited = [False]*9

# print(visited)

# dfs(graph,1,visited)


#bfs algorithm

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] =True


    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True

graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9
bfs(graph,1,visited)


'''
string.count('x') : 특정 string에 x가 몇번 포함되어있는지 세는 메써드
'''