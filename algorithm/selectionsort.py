"""
Selection sort
1. for stand in range(len(data_list)-1)
2. lowest=stand로 놓고
3. for num in range(stand, len(data_list)) stand 이후부터 반복
    내부 반복문 안에서 data_list[lowest]>data_list[num] 이면,
      lowest=num
4. data_list[num],data_list[lowest]=data_list[lowests],data_list[num]
반복문이 두개 , 시간복잡도는 O(n^2)이다.
"""

def selection_sort(data):
    for stand in range(len(data)-1):
        lowest=stand
        # 가장 작은값을 찾아 앞으로 옮기는 과정이다.
        for index in range(stand+1,len(data)):
            if data[lowest]>data[index]:
                lowest=index
        data[lowest],data[stand]=data[stand],data[lowest]
    return data

import random

data_list=random.sample(range(100),50)
print(data_list)
print(selection_sort(data_list))