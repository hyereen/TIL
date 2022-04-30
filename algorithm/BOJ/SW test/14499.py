# 주사위 굴리기
# 주사위 up 북 동 서 남 down 순서


n,m,x,y,k = map(int,input().split())

graph=[list(map(int,input().split())) for i in range(n)] 

dice=[0] * 6

order=list(map(int,input().split()))
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for i in range(k):
    d=int(order.pop(0))
    nx=x+dx[d-1]
    ny=y+dy[d-1]

    if 0<=nx<n and 0<=ny<m:
        if d==1:
            dice[0],dice[2],dice[3],dice[5]=dice[3],dice[0],dice[5],dice[2]
        elif d==2:
            dice[0],dice[2],dice[3],dice[5]=dice[2],dice[5],dice[0],dice[3]
        elif d==3:
            dice[0],dice[1],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[1]
        else:
            dice[0],dice[1],dice[4],dice[5]=dice[1],dice[5],dice[0],dice[4]

        if graph[nx][ny]==0:
            graph[nx][ny]=dice[5]
        else:
            dice[5]=graph[nx][ny]
            graph[nx][ny]=0

        x=nx
        y=ny
        print(dice[0])
    else:
        continue 