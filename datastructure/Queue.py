"""
큐는 줄을 서는 행위와 유사하다.
일반적으로 가장 먼저 넣은 데이터를 가장 먼저 꺼낼수 있는 구조(FIFO (First In First Out))
(스택 과 반대 , 스택은 LIFO (Last In First Out) , 스택은 책을 쌓는 구조라고 생각)
딱히 장단점은 없고 큐는 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용된다는 것을 기억
"""

# 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
### 1. Queue() (가장 일반적인 큐 ,FIFO(First-In,First-Out))
import queue

data_queue=queue.Queue()

data_queue.put("funding") # 큐에서 .put 함수를 사용할때는 문자열 숫자 모두 집어넣을수 있다.
data_queue.put(12)
print(data_queue.qsize()) # .put 은 괄호 안에 데이터를 넣어줘야하지만 qsize와 get은 인자가 필요하지 않다.
print(data_queue.get()) # .get() 을 통하여 데이터를 꺼내게 되면은 사이즈가 하나 줄어들게된다.
print(data_queue.qsize())
print(data_queue.get())

### 2. LifoQueue() (LIFO(Last-in.First-Out) , 스택 이랑 같은 LIFO 이다.)
import queue

data_queue=queue.LifoQueue()

data_queue.put("funding")
data_queue.put("12")
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
# 일반적인 Queue 와 반대로 마지막에 넣은 12부터 꺼내지게 된다.

### 3. PriorityQueue() (우선순위큐 , 데이터를 넣어줄때 튜플로 우선순위 번호와 함께 데이터를 넣어준다.)
import queue

data_queue=queue.PriorityQueue()

data_queue.put((10,"사과"))
data_queue.put((5,1))
data_queue.put((15,"수박"))
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())
# 우선순위는 등수라고 생각 1등에 가까울수록 빨리 꺼내진다. (5,1),(10,"사과"),(15,"수박") 순으로 출력된다.

# 큐는 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용된다.

### 리스트 변수로 큐를 다루는 enqueue,dequeue 기능 구현해보기
queue_list=list() # list() 비어있는 리스트를 생성 시켜준다.

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data=queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))

print(dequeue())
print(dequeue())



