"""
Bubble sort
1. for num in range(len(data_list)) 반복
2. swap = 0 (교환이 되었는지를 확인하는 변수를 둔다.)
3. 반복문 안에서 , for index in range(len(data_list)-num-1) n-1번 반복해야 하므로
4. 반목문안의 반복문 안에서 if data_list[index] > data_list[index+1] 이면
5. data_list[index],data_list[index+1] = data_list[index+1],data_list[index]
6. swap +=1
7. 반복문 안에서 if swap == 0 이면 break

반복문이 두개 , 시간복잡도는 O(n^2)이다.
"""

def bubblesort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            if data[index2]>data[index2+1]:
                data[index2],data[index2+1]=data[index2+1],data[index2]
                swap=True

        if swap == False:
            break
        # 바뀐게 없다면 이미 다 정렬되어져 있다는 뜻이다.
    return data

import random

data_list=random.sample(range(100),50)
print(data_list)
print(bubblesort(data_list))