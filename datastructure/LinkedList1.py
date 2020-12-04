class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Nodemgmt:
    def __init__(self,data):
        self.head=Node(data)

    def add(self,data):
        node=self.head
        while node.next:
            node=node.next
        node.next=Node(data)

    def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

    def delete(self,data):
        if self.head=="":
            print("저장된 데이터가 없습니다.")
            return

        if self.head.data==data:
            temp=self.head
            self.head=self.head.next
            del temp
        else:
            node=self.head
            while node.next:
                if node.next.data==data:
                    temp=node.next
                    node.next=node.next.next
                    del temp
                else:
                    node=node.next

    def search_node(self,data):
        node=self.head
        while node:
            if node.data==data:
                print("해당되는 노드가 있습니다.")
                print(node.data)
                return
            else:
                node=node.next

linked_list1=Nodemgmt(0)
linked_list1.desc()
for i in range(1,10):
    linked_list1.add(i)
linked_list1.desc()
linked_list1.delete(0)
linked_list1.delete(4)
linked_list1.desc()
linked_list1.search_node(8)