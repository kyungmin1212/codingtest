'''
그리디 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법
ex) 거스름돈 문제
'''

n=1260
count=0
coin_types=[500,100,50,10]

for coin in coin_types:
    count+=n//coin
    n%=coin
print(count)