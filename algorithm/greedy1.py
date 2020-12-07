"""
큰 수의 법칙
ex) M=8 K=3 / 2 4 5 4 6 ==> 66656665
    M=7 K=2 / 3 4 3 4 3 ==> 4444444
    같은 인덱스번호의 요소가 k번 이상 나오면 안되게 m번 더하라.
입력 : 첫째 줄에는 N M K 자연수
      둘째 줄에는 N개의 자연수 (K<=M)
출력 : 큰수의 법칙에 의해 더해진 답을 구해라
"""
import sys
n,m,k=map(int,sys.stdin.readline().split())
arr=[int(x) for x in sys.stdin.readline().split()]
arr=sorted(arr,reverse=True)
a=m//(k+1)
b=m%(k+1)
result=(arr[0]*k+arr[1])*a+arr[0]*b
print(result)
