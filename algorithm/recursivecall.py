"""
recursive call
함수안에서 동일한 함수를 호출하는 형태
재귀호출은 스택의 전형적인 예이다 하나씩 쌓고 제일 최근에 쌓은거부터 꺼내간다.
파이썬의 재귀함수는 깊이가 1000회 이하여야 한다.
ex ) 팩토리얼
"""

# 팩토리얼
def factorial(num):
    if num>1:
        return num*factorial(num-1)
    else:
        return num

for num in range(11):
    print(factorial(num))


# 재귀함수를 활용해서 1부터 num 까지의 곱이 출력되게 하라
def multiple(data):
    if data>1:
        return data*multiple(data-1)
    else:
        return data

print(multiple(10))

# 재귀함수를 이용해 숫자가 들어 있는 리스트의 합을 리턴하는 함수를 만들기
import random
data=random.sample(range(100),10)
print(data)

def sum_list(data):
    if len(data)>1:
        return data[0]+sum_list(data[1:])
    else:
        return data[0]
print(sum_list(data))

# 재귀함수를 이용해 회문(palindrome)을 판별할수 있는 함수를 리스트 슬라이싱을 활용해서 만들기(level,ata)
def palindrome(string):
    if len(string)<=1:
        return True
    if string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

print(palindrome("level"))
print(palindrome("abc"))

# 프로그래밍 연습(n이 홀수면 3xn+1 , n이 짝수면 n을 2로 나눈다 .결국 1이 될때 까지 2와 3의 과정을 반복한다.과정모두출력)
def func(n):
    print(n)
    if n==1:
        return n

    if n%2==0:
        return func(int(n/2))
    elif n%2==1:
        return func(3*n+1)

func(3)

# 프로그래밍 연습
# (정수 4를 1, 2, 3 의 조합으로 나타내는 방법은 총 7가지가 있다. n 이 주어졌을때 1,2,3의 합으로 나타내는 방법수)
# (1+1+1+1,1+1+2,1+2+1,2+1+1,2+2,1+3,3+1)

def func1(data):
    if data==1:
        return 1
    elif data==2:
        return 2
    elif data==3:
        return 4
    return func1(data-1)+func1(data-2)+func1(data-3)

print(func1(5))