"""
1이 될때 까지
문제 : N이 1이 될때까지 다음 두개의 연산중 하나를 수행한다 (단 2. 는 나누어떨이질때만)
 1. N에서 1을 뺀다.
 2. N을 K로 나눈다.
ex) n=17 k=4 n을 1로 만드는 최소횟수는 3이 된다. (17-1)->(16/4)->(4/4) 총 3번 진행했다.
입력 : 첫째 줄에 N과 K 가 주어진다.
출력 : N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
"""
import sys
n,k=map(int,sys.stdin.readline().split())
def minus(data):
    return data-1
def divide(data):
    return data/k
num=0
while n!=1:
    if n%k==0:
        n=divide(n)
    else:
        n=minus(n)
    num+=1
print(num)