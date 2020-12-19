"""
 퀵정렬(quick sort) (분할정복(Divide and Conquer))
- 정렬 알고리즘의 꽃
- 기준점(pivot)을 정해서 기준점보다 작은 데이터는 왼쪽(left) 큰 데이터는 오른쪽(right)으로 모으는 함수를 만든다.
- 각 왼쪽(left) 오른쪽(right)는 재귀용법을 사용해서 다시 동일 함수를 호출하는 작업을 반복한다.

- quicksort 함수 만들기
    만약 리스트 갯수가 한개이면 해당 리스트 리턴
    그렇지 않으면 리스트 맨앞의 데이터를 기준점(pivot)으로 놓기
    left right 리스트 변수를 만들고
    맨 앞의 데이터를 뺀 나머지 데이터를 기준점과 비교(pivot)
        기준점보다 작으면 left.append(해당데이터)
        기준점보다 크면 right.append(해당데이터)
    return quicksort(left) + pivot + quicksort(right) 로 재귀 호출

- 시간복잡도는 O(nlogn)이다. (병합정렬과 동일 웬만한경우에는 병합정렬보다 빠르다고 알려져있다.)
- 최악의 경우가 O(n^2) 이다.
"""
#
# def qsort(data):
#     if len(data)<=1:
#         return data
#
#     left,right=list(),list()
#     pivot=data[0]
#
#     for i in range(1,len(data)):
#         if data[i]<pivot:
#             left.append(data[i])
#         else:
#             right.append(data[i])
#
#     return qsort(left)+[pivot]+qsort(right)



# list comprehension 으로 깔끔하게 만들어보기
def qsort(data):
    if len(data)<=1:
        return data

    left,right=list(),list()
    pivot=data[0]
    left=[data[i] for i in range(1,len(data)) if data[i]<pivot]
    right=[data[i] for i in range(1,len(data)) if data[i]>=pivot]

    return qsort(left)+[pivot]+qsort(right)

import random

data_list=random.sample(range(100),50)
print(qsort(data_list))