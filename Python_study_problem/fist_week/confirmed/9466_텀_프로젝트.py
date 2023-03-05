
import sys
input = sys.stdin.readline

def DFS_cycle(E, Visit_table, Process_table, V, Num, valid) : 
    
    if Process_table[V] and Visit_table[V] != 0 : 
        Process_table[V] = False
        return True, V, Num

    if not valid and Visit_table[V] != 0 : 
        Process_table[V] = False
        return False, -1, -1

    Visit_table[V] += 1
    Process_table[V] = True

    Cycle, index, node_num = DFS_cycle(E, Visit_table, Process_table, E[V] - 1,  Num + 1, valid)
    Process_table[V] = False

    return Cycle, index, node_num


def solution() -> int : 
    N = int(input())
    E = list(map(int, input().split()))
    
    Visit_table = [0 for _ in range(N)]
    Process_table = [False for _ in range(N)]

    count = N
    for i in range(N) : 
        
        if Visit_table[i] != 0 : continue
        Cycle, index, node_num = DFS_cycle(E, Visit_table, Process_table, i, 0, False)
        
        if Cycle and Visit_table[index] == 1 : 
            count -= DFS_cycle(E, Visit_table, Process_table, index, 0, True)[2]
    
    return count


if __name__ == '__main__' : 
    
    Result = []

    for _ in range(int(input())) : 
        Result.append(solution())
    
    for value in Result : 
        print(value)



# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(111111)

# def dfs(node):
    
#     global answer
#     visited[node]=True
#     cycle.append(node)
#     nxt = graph[node]
    
#     if visited[nxt]:
#         if nxt in cycle:
#             answer -= (len(cycle)-cycle.index(nxt)) 
#             return
        
#     if not visited[nxt]:
#         dfs(nxt)

# for _ in range(int(input())): # 테스트케이스
#     n = int(input())
#     graph = [-1]+list(map(int,input().split()))
#     visited = [False]*(n+1) # 1번부터 시작
#     answer = n
#     for x in range(1,n+1):
#         if not visited[x]:
#             cycle = []
#             dfs(x)
#     print(answer)