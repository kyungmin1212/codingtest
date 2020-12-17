"""
상하좌우
문제 : NxN 정사각형 공간 , 1x1크기의 정사각형으로 나누어져있다. 가장 왼쪽 위 좌표는 (1,1) 오른쪽아래는 (N,N)
시작 좌표는 항상 (1,1) 이다.
L:왼쪽으로 한칸 이동 R:오른쪽으로 한칸 이동 U:위로 한칸 이동 D:아래로 한칸이동
NxN 을 벗어나는 움직임은 무시된다.
최종 도착할 지점의 좌표를 출력하시오
입력 : 첫째줄에는 공간의 크기 N
둘째 줄에는 여행가 A가 이동할계획서 내용 (ex R R R U D D)
출력 : 도착할 지점의 좌표
"""
import sys
n=int(sys.stdin.readline())
arr=[x for x in sys.stdin.readline().split()]

now=[1,1]
for i in arr:
    if i=='D' and now[0]<=n-1:
        now[0]+=1
    elif i=="U" and now[0]>=2:
        now[0]-=1
    elif i=="L" and now[1]>=2:
        now[1]-=1
    elif i=="R" and now[1]<=n-1:
        now[1] += 1
print(now[0],now[1])