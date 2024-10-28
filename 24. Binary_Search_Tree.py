class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right

class Tree:
    def __init__(self,root=None):
        self.root=root
    
    def insert_item(self,item):
        self.item=item
        if self.root is None:
            self.root=Node(None,self.item,None)
        else:
            self.item.left= 