"""
동적계획법(DP)
- 입력 크기가 작은 부분 문제들을 해결한후 해당 부분 문제의 해를 활용해서 보다 큰 크기의 부분 문제를 해결
- 상향식 접근법
- Memorization 기법 사용
ex) 피보나치수열
"""
# 피보나치수열 (recursive call 활용)
def fibo(num):
    if num<=1:
        return num
    return fibo(num-1)+fibo(num-2)

# 피보나치수열 (동적계획법사용)
def fibo_dp(num):
    cache=[0 for index in range(num+1)]
    cache[0]=0
    cache[1]=1

    for index in range(2,num+1):
        cache[index]=cache[index-1]+cache[index-2]
    return cache[num]
# 동일한 값들을 계속 계산해야하는 과저을 줄여주므로 속도가 더빨라진다.

print(fibo(10))
print(fibo_dp(10))