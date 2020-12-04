# 노드 삽입과 검색이 있는경우
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class NodeMgmt:
    def __init__(self,value):
        self.head=Node(value)

    def insert(self,value):
        self.current_node=self.head
        while True:
            if value<self.current_node.value:
                if self.current_node.left!=None:
                    self.current_node=self.current_node.left
                else:
                    self.current_node.left=Node(value)
                    break
            else:
                if self.current_node.right!=None:
                    self.current_node=self.current_node.right
                else:
                    self.current_node.right=Node(value)
                    break

    def search(self,value):
        self.current_node=self.head
        while True:
            if value==self.current_node.value:
                return True
            elif value<self.current_node.value:
                if self.current_node.left!=None:
                    self.current_node=self.current_node.left
                else:
                    return False
            else:
                if self.current_node.right!=None:
                    self.current_node=self.current_node.right
                else:
                    return False


BST=NodeMgmt(10)
BST.insert(2)
BST.insert(1)
BST.insert(9)
print(BST.search(9))
print(BST.search(10))
print(BST.search(2))
print(BST.search(-1))