class Heap:
    def __init__(self,data):
        self.heap_array=list()
        self.heap_array.append(None)
        self.heap_array.append(data)
        # None 을 넣어주는 이유는 Heap 구현을 편하게 하기위하여 배열 인덱스를 1부터 사용하기 위함이다.

    def move_up(self,inserted_idx):
        if inserted_idx<=1:
            return False
        parent_idx=inserted_idx//2
        if self.heap_array[inserted_idx]>self.heap_array[parent_idx]:
            return True
        else:
            return False
        # True 인경우에는 입력된 값이 부모노드보다 값이 크므로 위치를 변경해야하는 경우다

    def insert(self,data):
        if len(self.heap_array)==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        # 일종의 방어 코드이다.

        self.heap_array.append(data)

        inserted_idx=len(self.heap_array)-1
        # self.heap_array 의 길이는 None 을 포함하기때문에 1이 더늘어난다 그러므로 1을 빼준다.

        while self.move_up(inserted_idx): # 자리를 바꿔야 하는 경우만 while 문 반복
            parent_idx=inserted_idx//2
            self.heap_array[inserted_idx],self.heap_array[parent_idx]=self.heap_array[parent_idx],self.heap_array[inserted_idx]
            inserted_idx=parent_idx
        return True
        #True 가 된경우는 삽입이 됐다는 뜻

    def move_down(self,popped_idx):
        left_child_popped_idx=popped_idx*2
        right_child_popped_idx=popped_idx*2+1
        # len(self.heap_array) 랑 값을 비교할때 =등호가 들어가는 이유는 self.heap_array 가 None 을 포함하고 있으므로 길이가 1이 더길기때문이다.
        # case 1 왼쪽 오른쪽 둘다 없는경우(왼쪽만 없는경우를 고려하면된다. 힙은 왼쪽부터채우므로)
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case 2 오른쪽 자식 노드만 없는경우
        elif right_child_popped_idx >=len(self.heap_array):
            if self.heap_array[popped_idx]<self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # case 3 왼쪽 오른쪽 둘다 있는 경우
        else:
            if self.heap_array[left_child_popped_idx]>self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx]<self.heap_array[left_child_popped_idx]:
                    return True
                # 왼쪽 오른쪽 둘중에 큰값하고만 바꿔야하므로 left 가 클때는 left 랑만 비교한다.
                else:
                    return False
            else:
                if self.heap_array[popped_idx]<self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array)<=1:
            return None
        # heap_array 는 None 부터 시작하므로 길이가 1보다 작다면 이거는 None 밖에 없는경우다 그래서 꺼낼것이 없으므로 None 을 return 한다.

        returned_data=self.heap_array[1]
        # max 값이 1번째 인덱스에 위치하므로 self.heap_array[1]이다
        self.heap_array[1]=self.heap_array[-1]
        # 제일 마지막에 들어간 값과 최고값의 위치를 바꿔준다.
        del self.heap_array[-1]
        popped_idx=1
        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case1 은 왼쪽 노드도 없으므로 바꿀게 없으니까 고려할필요가 없다 False 를 반환하므로

            # case 2 왼쪽 자식 노드만 있는경우
            if right_child_popped_idx>=len(self.heap_array):
                if self.heap_array[popped_idx]<self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]=self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                    popped_idx=left_child_popped_idx

            # case 3 왼쪽 오른쪽 둘다있는경우
            else:
                if self.heap_array[left_child_popped_idx]>self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx]<self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]=self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                        popped_idx=left_child_popped_idx
                else:
                    if self.heap_array[popped_idx]<self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx],self.heap_array[right_child_popped_idx]=self.heap_array[right_child_popped_idx],self.heap_array[popped_idx]
                        popped_idx=right_child_popped_idx
        return returned_data

heap=Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(120)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
