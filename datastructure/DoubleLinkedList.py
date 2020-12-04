class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class NodeMgmt:
    def __init__(self,data):
        self.head=Node(data)
        self.tail=self.head

    def insert(self,data):
        if self.head=="":
            self.head=Node(data)
            self.tail=self.head
        else:
            node=self.head
            while node.next:
                node=node.next
            new=Node(data)
            self.tail=new
            new.prev=node
            node.next=new


    def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

    def search_from_head(self,data):
        if self.head=="":
            print("링크드 리스트 안에 데이터가 존재하지 않습니다.")
        else:
            node=self.head
            while node.data!=data:
                node=node.next
                if node==None:
                    return False
            print("링크드 리스트 안에 데이터가 존재합니다 ",node.data)

    def search_from_tail(self,data):
        if self.head=="":
            print("링크드 리스트 안에 데이터가 존재하지 않습니다.")
        else:
            node=self.tail
            while node.data!=data:
                node=node.prev
                if node==None:
                    return False
            print("링크드 리스트 안에 데이터가 존재합니다.",node.data)

    def insert_before(self,data,before_data):
        if self.head=="":
            self.head=Node(data)
            self.tail=self.head
        else:
            node=self.tail
            while node.data!=before_data:
                node=node.prev
                if node==None:
                    return False
            new=Node(data)
            before_new=node.prev
            new.prev=before_new
            new.next=node
            node.prev=new
            if before_new==None:
                self.head=new
            else:
                before_new.next=new

    def insert_after(self,data,after_data):
        if self.head=="":
            self.head=Node(data)
            self.tail=self.head
        else:
            node=self.head
            while node.data!=after_data:
                node=node.next
                if node==None:
                    return False
            new=Node(data)
            after_new=node.next
            new.prev=node
            new.next=after_new
            node.next=new

            if after_new==None:
                self.tail=new
            else:
                after_new.prev=new

node_mgmt=NodeMgmt(0)
for data in range(1,10):
    node_mgmt.insert(data)

node_mgmt.desc()
node_mgmt.insert_after(1.5,1)
node_mgmt.insert_before(2.5,3)
node_mgmt.desc()