"""
숫자 카드게임
ex) 3 1 2
    4 1 4
    2 2 2
NxM 형태로 카드가 놓여있다. 행을 하나 골라서 그중 가장 작은 값이 내가 뽑은 카드이다.
최종적으로 가장 작은 숫자가 큰 행을 고르면 이길수있다.
입력 : 첫째 줄에는 N 과 M
 둘째 줄에는 N줄에 걸쳐 각 카드에 적힌 숫자가 주어진다.
출력 : 게임룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
"""
import sys
N,M=map(int,sys.stdin.readline().split())
arr=[]
for i in range(N):
    arr.append(sys.stdin.readline().split())
a=[]
for j in arr:
    a.append(min(j))
print(max(a))