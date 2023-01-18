# https://www.acmicpc.net/source/53218789

import sys
input=sys.stdin.readline

def DFS(x,y,country):
    if x<0 or x>=N or y<0 or y>=M: # 그리드 밖으로가면 종료
        return 0

    if not visit[x][y] and graph[x][y]: #방문하지 않았고 섬이라면
        visit[x][y]=country #섬 번호를 붙여준다
        bridge.append((x,y,country)) # 섬인 지점에 대해서 모두 좌표값을 추가한다.

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]
            DFS(nx,ny,country)

    return 0

def distance():

    for i in bridge: #모든 섬인 지점으로부터 길이를 탐색한다.
        x,y,country=i # 좌표값과 섬 번호를 저장한다

        for j in range(4):

            length=0 # 섬과 섬 사이의 거리를 담는다
            nx=x+dx[j] ; ny=y+dy[j] #방향

            while True:

                if nx<0 or nx>=N or ny<0 or ny>=M: # 그리드 밖으로가면 종료
                    break

                if country==visit[nx][ny]: #자신과 똑같은 섬은 연결할 필요가없다
                    break

                if not visit[nx][ny]: # 만약 섬이 아니라 바다라면 , 즉 값이 0 이라면
                    nx+=dx[j] ; ny+=dy[j] # 똑같은 방향을 추가한다.
                    length+=1 # 길이추가
                    continue # 계속 탐색한다.
                if length<2: # 다리의 길이가 2보다 작으면 추가하지않는다.
                    break

                edges.append( (length,country,visit[nx][ny]) ) # 두 섬을 연결하는 최소값을 저장한다.
                break # 최소값을 저장하면 바로 break 를 통해 나가준다.

def Find(x): # 유니온 파인드의 Find 함수. 최상위 부모를 찾는다.

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])
    return disjoint[x]

def Union(a,b): # 유니온 파인드의 Union 함수 , 두 집합을 같은 집합으로 묶는다.

    a=Find(a)
    b=Find(b)

    if a>b:
        disjoint[a]=b
    else:
        disjoint[b]=a


dx=[0,0,1,-1]
dy=[-1,1,0,0] # 상하좌우 방향 좌표값

N,M=map(int,input().split()) # N , M 입력
graph=[ list(map(int,input().split())) for _ in range(N) ] #그래프 입력

visit=[ [0]*M for _ in range(N) ] # 방문 처리배열
country=0 ; bridge=[] ; edges=[] ; answer=0 ; count=0

#섬의 번호 , 연결할수 있는 좌표 , 간선 , 정답을 담을 배열 ,  간선의 개수 저장변수

for i in range(N):
    for j in range(M):
        if not visit[i][j] and graph[i][j]==1: #만약 방문하지 않은 지점이고 섬이라면
            country+=1 # 섬번호를 추가하고
            DFS(i,j,country) # 탐색을 시작한다  , 모든 섬에대해 번호를 붙여준다.
            


disjoint=[ _ for _ in range(country+1) ] # 유니온 파인드에서 최상위 부모를 저장할 배열

distance() # 모든 섬들에 대해서 거리의 최소값을 찾는다.
edges.sort(key=lambda x:x[0]) # 거리에 대하여 정렬

for i in edges: #모든 두 선을 연결하는 좌표에 대해서

    length,x,y,=i #길이와 좌표값을 저장한다.

    if Find(x)!=Find(y): #서로 다른 집합이라면
        Union(x,y) # 집합을 합친다.
        answer+=length # 거리를 더해준다.
        count+=1 # 횟수를 더해준다.

if count==country-1: # 만약 연결한 횟수가 나라의 개수만큼 같다면 , country 번호는 2부터 시작해서 1을 뺴야함.
    print(answer) # 결과 출력
else:
    print(-1) # 연결할수 없을 경우 -1 출력