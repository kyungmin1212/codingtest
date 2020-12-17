"""
Insertion sort
1. for stand in range(len(data_list)) 로 반복
2. key = data_list[stand]
3. for num in range(stand,0,-1) 반복
    내부 반복문 안에서 data_list[stand]<data_list[num-1]이면
        data_list[num-1],data_list[num]=data_list[num],data_list[num-1]
반복문이 두개 , 시간복잡도는 O(n^2)이다.
"""

def insertion_sort(data):
    for index in range(len(data)-1):
        # index2 는 index+1 부터 1까지를 말한다 마지막 0은 포함안함
        for index2 in range(index+1,0,-1):
            if data[index2]<data[index2-1]:
                data[index2],data[index2-1]=data[index2-1],data[index2]
            # 앞으로 가다가 자기보다 작은거를 발견하면 그냥 멈추면된다. 위치를 바꿀필요가없음
            else:
                break
    return data

import random

data_list=random.sample(range(100),50)
print(data_list)
print(insertion_sort(data_list))