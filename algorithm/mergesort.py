"""
병합정렬(merge sort)  (분할정복(Divide and Conquer))
- 재귀용법을 활용한 정렬 알고리즘
- 각 원소를 하나하나 다떨어뜨려놓은 다음 2개씩 크기 비교를 하면서 차근차근 병합해나가는 과정

1. sorted_list 리스트 변수 선언하기
2. left_index,right_index 를 0으로 초기화하기
3. while left_index < len(left) or right_index <len(right) 이면
    - 만약 left_index>=len(left) 이면 ,sorted_list에 right[right_index]를 추가하고 , right_index 값을 1증가
    - 만약 right_index>=len(right)이면 , sorted_list 에 left[left_index]를 추가하고 ,left_index 값을 1증가
    - 만약 left[left_index]<right([right_index]이면, sorted_list 에 left[left_index]를 추가하고 left_index 값 1증가
    - 위 세가지가 아니면 sorted_list에 right[right_index]를 추가하고 right_index 값 1 증가

- 시간복잡도는 O(nlogn)이다.
"""

def mergesplit(data):
    if len(data)<=1:
        return data
    medium=int(len(data)/2)
    left=mergesplit(data[:medium])
    right=mergesplit(data[medium:])
    return merge(left,right)

def merge(left,right):
    left_index=0
    right_index=0
    result=[]
    while len(left)>left_index and len(right)>right_index:
        if left[left_index]>right[right_index]:
            result.append(right[right_index])
            right_index+=1
        else:
            result.append(left[left_index])
            left_index+=1
    # 위의 반복문으로 left 나 right 둘중에 하나는 값이 다 result 안에 들어가게 된다.
    # 남은경우는 둘중에 하나만 남은경우다.
    while len(left)>left_index:
        result.append(left[left_index])
        left_index+=1

    while len(right)>right_index:
        result.append(right[right_index])
        right_index+=1

    return result

import random
data_list=random.sample(range(100),11)
print(mergesplit(data_list))