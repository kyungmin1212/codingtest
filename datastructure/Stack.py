"""
데이터를 제한적으로 접근할 수 있는 구조 (한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조)
가장 나중에 쌓은 데이터를 가장 먼저 빼낼수 있는 데이터 구조 ( 책을 쌓으면 제일 위에 있는 책을 꺼내는것 처럼 생각)
(큐는 FIFO , 스택은 LIFO )
스택 구조는 프로세스 실행 구조의 가장 기본
장점 : 구조가 단순해서 구현이 쉽다.
      데이터 저장/읽기 속도가 빠르다.
단점(일반적인 스택 구현시) : 데이터 최대 갯수를 미리 정해야한다. (파이썬의 경우 재귀함수는 1000번까지만 호출가능),
                         저장공간의 낭비가 발생할수 있다.(미리 최대 갯수만큼 저장공간을 확보했기 때문이다.)
스택은 단순하고 빠른 성능을 위해 사용되므로 , 보통 배열 구조를 활용해서 구현하는 것이 일반적이다.
"""

# 재귀함수
def recursive(data):
    if data<0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned",data)

recursive(4)

"""
 프로그램 작동 방식을 살펴보면
 recursive(4)->print(4)->recursive(3)(아직 recursive(4)가 끝난것이 아니다.)->print(3)
 ->recursive(2)(아직 recursive(3) 과 recursive(4)가 끝난것이 아니다.)-> print(2)->recursive(1)
 ->print(1)->recursive(0)->print(0)->recursive(-1)->"ended"->미처끝나지 않은 recursive(0)의 print("returned",data)를 실행한다.
 ->recursive(1)->recursive(2)->recursive(3)->recursive(4)
 4부터 -1 까지 차근차근 쌓았다가 다시 -1부터 4까지 갔다. 이러한 과정을 Process Stack 이라고 한다.
"""

# 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기 (append(push),pop 메서드 제공)

data_stack=list()

data_stack.append(1)
data_stack.append(2)
print(data_stack)
print(data_stack.pop())
# 제일 마지막에 넣은 데이터(여기서는 2)를 꺼내고 삭제시켜준다.

# 리스트 변수로 스택을 다루는 pop,push 기능 구현해보기
stack_list=list()

def push(data):
    stack_list.append(data)

def pop():
    data=stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)
print(stack_list)
print(pop())
print(stack_list)