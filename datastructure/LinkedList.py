"""
링크드 리스트(Linked List) ( 연결 리스트 )
배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
본래 C언어에서는 주요한 데이터 구조이지만 ,파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원
링크드 리스트 기본구조와 용어
-노드(Node, 데이터값,포인터 로 구성) 와 포인터(pointer, 각 노드 안에서 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간)
배열은 미리 특정한 연결된 공간을 예약을 해두고 거기다가 데이터를 쓰고 읽는 그런 구조이고
이에 반해 링크드 리스트는 미리 예약을 안해놓고 필요할때마다 데이터를 추가 할수 있는 구조다
일종의 배열의 단점을 극복한 자료구조가 링크드 리스트이다.
(A,주소) (B,주소) A의 주소가 B를 가르키면 연결된다. B의 주소가 지정하는것이 없으면 데이터는 거기서 끝난다.
장점 : 미리 데이터 공간을 미리 할당하지 않아도 된다(cf 이에 반에 배열은 미리 데이터 공간을 할당해야한다.)
단점 : 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않다.
      연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다.
      중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업이 필요하다.
"""

# ### Node 구현 ###
# class Node():
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next
#
# # Node 와 Node 연결하기(포인터 활용)
# node1=Node(1)
# node2=Node(2)
# node1.next=node2
# head=node1
#
# ######
#
# ### 링크드 리스트로 데이터 추가하기 ###
# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next
#
# def add(data):
#     node=head  # head 노드 지정
#     while node.next: # head 노드의 next가 있을경우 실행
#         node=node.next # 다음 노드를 head 노드의 next 로 지정한다. 다시 와일문으로가서 다음노드의 넥스트가 존재하는지 확인 ->이과정 반복(노드의 다음주소가 없을때까지)
#     node.next=Node(data) # while 문이 끝났다는것은 노드의 다음 주소가 존재하지 않는다는것이다. 이때 다음주소를 노드 생성 클래스를 통해 생성된 노드로 지정해준다.
#
# node1=Node(1)
# head=node1 # head 노드를 지정해줘야한다.
# for index in range(2,10):
#     add(index)
#
# # 링크드 리스트 데이터 출력하기(검색하기)
# node=head
# while node.next:
#     print(node.data)
#     node=node.next
# print(node.data)
#
# # 링크드 리스트의 복잡한 기능1(링크드 리스트 데이터 사이에 데이터를 추가)
# node3=Node(2.5)
#
# node=head
# search=True
# while search:
#     if node.data ==2:
#         search =False
#     else:
#         node=node.next
#
# node_next=node.next
# node.next=node3
# node3.next=node_next
#
# node=head
# while node: # node.data 로 쓰면 오류날수도 있는것이 node.data 의 값이 0이 되면은 False로 인식해서 while 문이 실행되지 않는다.
#     print(node.data)
#     node=node.next
#
# ######

# ### 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기 ###
# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next
#
# class NodeMgmt:
#     def __init__(self,data):
#         self.head=Node(data)
#
#     def add(self,data):
#         if self.head=="": # self.head 는 NodeMgmt 가 실행될때 이미 만들어지지만 없을경우를 대비한 일종의 방어 코드이다.
#             self.head=Node(data)
#         else:
#             node=self.head
#             while node.next:
#                 node=node.next
#             node.next=Node(data)
#
#     def desc(self): #출력함수
#         node=self.head
#         while node: # node.data 로 쓰면 오류날수도 있는것이 node.data 의 값이 0이 되면은 False로 인식해서 while 문이 실행되지 않는다. node.data 말고 node 로 써줘야한다.
#             print(node.data)
#             node=node.next
#     def delete(self,data): #데이터 삭제
#         if self.head=="": # head 가 없으면 링크드 리스트가 구성되지 않았다.
#             print("해당 값을 가진 노드가 없습니다.")
#             return
#         if self.head.data==data: #제일 앞에있는 데이터를 삭제할경우
#             temp = self.head
#             self.head=self.head.next
#             del temp
#         else:
#             node=self.head
#             while node.next:
#                 if node.next.data==data:
#                     temp=node.next
#                     node.next=node.next.next
#                     del temp
#                     return
#                 else:
#                     node=node.next
#
#     def search_data(self,data): #데이터 찾기
#         node=self.head
#         while node:
#             if node.data==data:
#                 return node.data
#             else:
#                 node=node.next
#
#
#
# linked_list1=NodeMgmt(0)
# linked_list1.desc()
# linked_list1.delete(0)
# linked_list1.desc()
# linked_list1=NodeMgmt(0)
# for data in range(1,10):
#     linked_list1.add(data)
# linked_list1.desc()
# linked_list1.delete(5)
# linked_list1.desc()
# print(linked_list1.search_data(3))
#
# ######

### 더블 링크드 리스트 기본구조 ###
"""
더블링크드리스트(Doubly linked list)
이중 연결리스트라고도 한다.
장점 : 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능하다.
(만약 일반적인 링크드 리스트라고 한다면 노드가 만개이라면 맨마지막 데이터를 가져오기에는 엄청난 시간을 걸린다.)
(이를 극복하기 위하여 후반부에 있는 데이터는 뒤에서 부터가져올수 있도록 만든것이 더블링크드리스트이다.)
"""
class Node:
    def __init__(self,data,prev=None,next=None): #더블링크드리스트는 앞에도 연결해주는 주소가 필요하다.
        self.data=data
        self.prev=prev
        self.next=next

class NodeMgmt:
    def __init__(self,data):
        self.head=Node(data)
        self.tail=self.head # 처음시작할때는 노드가 1개이므로 head 와 tail 이 같다.

    def insert(self,data):
        if self.head==None: # 방어코드
            self.head=Node(data)
            self.tail=self.head
        else:
            node=self.head
            while node.next:
                node=node.next
            new=Node(data)
            node.next=new
            new.prev=node # 더블링크드리스트는 이전주소도 연결시켜줘야한다.
            self.tail=new # 뒤에 데이터가 추가되었으므로 tail을 다시 지정해줘야한다.

    def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

    def search_from_head(self,data):
        if self.head==None:
            return False

        node=self.head
        while node:
            if node.data==data:
                return node
            else:
                node=node.next
        return False  # 찾는 데이터가 없을경우는 False 가 반환된다.

    def search_from_tail(self,data):
        if self.tail==None:
            return False
        node=self.tail
        while node:
            if node.data==data:
                return node
            else:
                node=node.prev
        return False

    def insert_after(self,data,after_data):
        if self.head==None:
            self.head=Node(data)
        else:
            node=self.head
            while node.data!=after_data:
                node=node.next
                if node==None:
                    return False
            new=Node(data)
            after_new=node.next
            new.next=after_new
            new.prev=node
            node.next=new
            if new.next==None:
                self.tail=new
            else:
                after_new.prev = new
            return True

    def insert_before(self,data,before_data):
        if self.head==None:
            self.head=Node(data)
            return True
        else:
            node=self.tail
            while node.data!=before_data:
                node=node.prev
                if node==None:
                    return False # before_data 가 존재하지 않는경우를 말한다.
            new=Node(data) # 삽입하고 싶은 노드 생성
            before_new=node.prev #노드 전의 데이터
            before_new.next=new #노드전의 데이터의 다음노드를 삽입하고싶은노드로 만든다
            new.prev=before_new #뉴의 전을 노드전의 데이터로 연결해준다.
            new.next=node # 뉴의 다음코드를 노드 데이터로 지정한다.
            node.prev=new # 노드의 전데이터를 뉴로 연결시켜준다.
            return True # 연결시켜주는것이 많은 이유는 앞뒤로 한번씩 연결해줘야하므로 데이터 하나가생성되면 총 4개를 연결시켜줘야한다.
double_linked_list=NodeMgmt(0)
for data in range(1,10):
    double_linked_list.insert(data)
double_linked_list.desc()
node_3=double_linked_list.search_from_tail(3)
print(node_3.data)
double_linked_list.insert_before(1.5,2)
double_linked_list.desc()
double_linked_list.insert_after(2.5,8)
double_linked_list.desc()