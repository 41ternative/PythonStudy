import sys
read = sys.stdin.readline
T = int(read())
l=[]
cnt=0
sys.setrecursionlimit(10**4)
#우하향으로만 내려감 좌편상편 방향을 추가해줘야함
# 넘어가면 return
def dfs(graph, i, j):
    if i==M or j==N or i==-1 or j==-1:
        return False
    if graph[j][i]==1:
        graph[j][i]=0
        dfs(graph,i-1,j)
        dfs(graph,i,j-1)
        dfs(graph,i+1,j)
        dfs(graph,i,j+1)
        return True

for i in range(T):
    M,N,K = map(int,read().split())
    # 초기 배추밭 설정하기
    l = [[0] * M for _ in range(N)]
    # 배추 색칠하기
    for _ in range(K):
        i, j = map(int, read().split())
        l[j][i] = 1
    # # 배추밭 print하기
    # for row in l:
    #     print(row)

    #탐색
    for p in range(M):
        for q in range(N):
            if l[q][p] == 1:
                if dfs(l,p,q) == True:
                    cnt+=1
                #근처 1을 0으로 만드는 함수 dfs
                #dfs가 참을 유지하면 cnt를 더함
                #dfs는 경계밖에 도달하면 0을 반환함
    print(cnt)
    cnt = 0


