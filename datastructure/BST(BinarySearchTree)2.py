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
        while self.current_node:
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


    def delete(self,value):
        self.parent=self.head
        self.current_node=self.head
        searched=False
        while self.current_node:
            if self.current_node.value==value:
                searched=True
                break # 값을 찾았으면 거기서 멈추면된다. break가 없으면 무한 반복 되게 된다.
            elif value<self.current_node.value:
                self.parent=self.current_node
                self.current_node=self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched==False:
            return False
        # searched가 False 라면 그즉시 delete 함수는 False 를 반환한다.
        # searched가 True 인경우에는 찾은 노드가 current_node 가 되고 그 전의 노드가 parent 노드가 된다.
        # value=current_node.value 이다.

        # Case 1 : 삭제할 Node 가 Leaf Node 인경우
        if self.current_node.left==None and self.current_node.right==None:
            if value<self.parent.value:
                self.parent.left=None
            else:
                self.parent.right=None
            del self.current_node

        # Case 2 : 삭제할 Node 가 Child Node 한개를 가지고 있는경우
        # child 노드가 왼쪽에 있는경우
        elif self.current_node.left!=None and self.current_node.right==None:
            if value<self.parent:
                self.parent.left=self.current_node.left
            else:
                self.parent.right=self.current_node.left
        elif self.current_node.left==None and self.current_node.right!=None:
            if value<self.parent.value:
                self.parent.left=self.current_node.right
            else:
                self.parent.right=self.current_node.right

        # Case 3 : 삭제할 Node가 Child Node 를 두 개를 가지고 있을경우
        # 이경우는 항상 삭제할 노드의 오른쪽으로 한번 내려간다음에 그 오른쪽의 내려간 노드의 자식들을 왼쪽아래로 쭉 내려가서 제일 작은값을 찾아온다.
        # 처음에 오른쪽으로 내려가는것은 왼쪽것보다 큰값이 위에 올라와야하므로 오른쪽거중에서 값을 제일 작은 값을 찾아서 올리는것이다.
        elif self.current_node.left!=None and self.current_node.right!=None:
            # (case3-1) Node가 parent의 왼쪽인 경우
            if value<self.parent.value:
                self.change_node=self.current_node.right
                self.change_node_parent=self.current_node.right
                while self.change_node.left!=None:
                    self.change_node_parent=self.change_node
                    self.change_node=self.change_node.left
                # while 문이 끝나면 child 노드의 오른쪽 제일 왼쪽 끝값(self.change_node)을 찾았다
                # 왼쪽 끝값을 올릴려고하는데 그 끝값의 오른쪽 차일드 노드 값이 있으면 그거를 위와 연결해줘야한다.
                if self.change_node.right!=None:
                    self.change_node_parent.left=self.change_node.right
                else:
                    self.change_node_parent.left=None
                # 삭제하고자 하는 노드를 삭제하면 그공간이 생기는데 그공간에다가 방금 꺼내온 제일 작은 값인 self.change_node 를 연결시켜준다.
                self.parent.left=self.change_node
                self.change_node.right=self.current_node.right
                self.change_node.left=self.current_node.left
            # (case3-2) Node가 parent의 오른쪽인경우
            else:
                self.change_node=self.current_node.right
                self.change_node_parent=self.current_node.right
                while self.change_node.left!=None:
                    self.change_node_parent=self.change_node
                    self.change_node=self.change_node.left
                if self.change_node.right!=None:
                    self.change_node_parent.left=self.change_node.right
                else:
                    self.change_node_parent.left=None
                self.parent.right=self.change_node
                self.change_node.left=self.current_node.left
                self.change_node.right=self.current_node.right
        return True
        # True 인경우는 삭제된경우다.

import random
bst_nums=set()
while len(bst_nums)!=100:
    bst_nums.add(random.randint(0,999))

binary_tree=NodeMgmt(500)
for num in bst_nums:
    binary_tree.insert(num)

for num in bst_nums:
    if binary_tree.search(num)==False:
        print("search failed", num)

delete_nums=set()
bst_nums=list(bst_nums)
while len(delete_nums)!=10:
    delete_nums.add(bst_nums[random.randint(0,99)])

for del_num in delete_nums:
    if binary_tree.delete(del_num)==False:
        print("delete failed",del_num)