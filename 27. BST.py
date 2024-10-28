class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right
    
class BST:
    def __init__(self,root=None):
        self.root=root
        self.item_count=0

    def insert_loop(self,data):
        if self.root is None:
            self.root=Node(None,data,None)
        else:
            temp=self.root
            while temp is not None:
                if data < temp.item:
                    if temp.left is None:
                        temp.left=Node(None,data,None)
                    temp=temp.left
                elif data > temp.item:
                    if temp.right is None:
                        temp.right=Node(None,data,None)
                    temp=temp.right
    
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,curr_root,data):
        if curr_root is None:
            return Node(None,data,None)
        if curr_root.item > data:
            curr_root.left=self.rinsert(curr_root.left,data)
        elif curr_root.item < data:
            curr_root.right=self.rinsert(curr_root.right,data)
        return curr_root 
    

    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,curr_root,data):
        if curr_root is None or curr_root.item == data:
            return True
        if curr_root.item > data:
            return self.rsearch(curr_root.left,data)
        if curr_root.item < data:
            return self.rsearch(curr_root.right,data)
        else:
            return False
   
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,curr_root,result):
        if curr_root is not None:
            self.rinorder(curr_root.left,result)
            result.append(curr_root.item)
            self.rinorder(curr_root.right,result)
        
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result

    def rpreorder(self,curr_root,result):
        if curr_root is not None:
            result.append(curr_root.item)
            self.rpreorder(curr_root.left,result)
            self.rpreorder(curr_root.right,result)
        
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    
    def rpostorder(self,curr_root,result):
        if curr_root is not None:
            self.rpostorder(curr_root.left,result)
            self.rpostorder(curr_root.right,result)
            result.append(curr_root.item)
# Deletion Code
    def min_val(self,curr_root):
        current=curr_root
        while current.left is not None:
            current=current.left
        return current.item

    def max_val(self,curr_root):
        current=curr_root
        while current.right is not None:
            current=current.right
        return current.item
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)

    def rdelete(self,curr_root,data):
        #check if tree is empty
        if curr_root is None:
            return curr_root
        if curr_root.item > data:
            curr_root.left=self.rdelete(curr_root.left,data)
        elif curr_root.item < data:
            curr_root.right=self.rdelete(curr_root.right,data)
        else:
            if curr_root.left is None:
                return curr_root.right
            elif curr_root.right is None:
                return curr_root.left
            curr_root.item=self.max_val(curr_root.right)
            self.rdelete(curr_root.right,curr_root.item)
        return curr_root
    
    
    
    
    def size(self):
        return len(self.inorder())





            

mybst=BST()
mybst.insert(40)
mybst.insert(30)
mybst.insert(50)
mybst.insert(25)
mybst.insert(35)
mybst.insert(45)
mybst.insert(60)
mybst.insert(28)

print(mybst.inorder())
mybst.delete(50)
print(mybst.inorder())


                