class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start
#========================== Print All Elements==================================
    def return_elements(self):
        
        if self.start is None:
            pass
        elif self.start is not None:
            print(self.start.item)
            start=self.start.next
            if self.start.next is not None:
                while start is not self.start:
                    print(start.item)
                    start=start.next
#============================ Insertion Code ===================================
   
    # Insert an Element at Start
    def insert_at_start(self,data):
        self.data=data
        newNode=Node(None,self.data,None)
        if self.start is None:
            self.start=newNode
        elif self.start.prev is None:
            self.start.next=newNode
            newNode.next=self.start
            newNode.prev=self.start
            self.start.prev=newNode
            self.start=newNode
        else:
            self.start.prev.next=newNode
            newNode.prev=self.start.prev
            self.start.prev=newNode
            newNode.next=self.start
            self.start=newNode

            
    #Insert an Element at Last
    def insert_at_last(self,data):
        self.data=data
        newNode=Node(None,self.data,None)
        if self.start is None:
            self.start=newNode
        elif self.start.prev is None:
            self.start.prev=newNode
            self.start.next=newNode
            newNode.next=self.start
            newNode.prev=self.start
        else: 
            self.start.prev.next=newNode
            newNode.prev=self.start.prev
            newNode.next=self.start
            self.start.prev=newNode

    #Insert After
    def insert_after(self,after,data):
        self.data=data
        self.after=after
        newNode=Node(None,self.data,None)
        if self.start.item is self.after: 
            if self.start.prev is None:
                self.start.next=newNode
                self.start.prev=newNode
                newNode.next=self.start
                newNode.prev=self.start
            else:
                newNode.next=self.start.next
                newNode.prev=self.start
                self.start.next.prev=newNode
                self.start.next=newNode
        else:
            temp=self.start.next
            while temp is not self.start:
                if temp.item is self.after:
                    newNode.next=temp.next
                    temp.next.prev=newNode
                    temp.next=newNode
                    newNode.prev=temp
                    break
                temp=temp.next
 #============================ Deletion Code ===================================
    # Delete First
    def delete_first(self):
        if self.start is None:
            pass
        elif self.start.prev is None:
            self.start=None
        elif self.start.next.next is self.start:
            self.start=self.start.next
            self.start.prev=None
            self.start.next=None
        else:
            self.start.next.prev=self.start.prev
            self.start.prev.next=self.start.next
            self.start=self.start.next
    
    # Delete Last
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.prev is None:
            self.start=None
        elif self.start.next.next is self.start:
            self.start.next.next=None
            self.start.next.prev=None
            self.start=self.start.next
        else:
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev
    
    #Delete item
    def delete_item(self,data):
        self.data=data
        if self.start.item is self.data:
            if self.start.prev is None:
                self.start=None
            elif self.start.next.next is self.start:
                self.start=self.start.next
                self.start.prev=None
                self.start.next=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
        else:
            temp=self.start.next
            while temp is not self.start:
                if temp.item is self.data:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    break
                temp=temp.next


        
    


mycdll=CDLL()
mycdll.insert_at_last(5)
mycdll.insert_at_last(6)
mycdll.insert_at_last(7)
mycdll.insert_at_last(8)
mycdll.insert_at_last(9)
mycdll.insert_at_last(10)
mycdll.insert_at_last(11)
mycdll.insert_at_last(12)
mycdll.insert_at_last(13)
mycdll.insert_at_last(14)
mycdll.insert_at_last(15)

mycdll.return_elements()
mycdll.delete_item(5)
mycdll.delete_item(6)
mycdll.delete_item(7)
mycdll.delete_item(8)
mycdll.delete_item(9)
mycdll.delete_item(10)
mycdll.delete_item(11)
mycdll.delete_item(12)
mycdll.delete_item(13)
mycdll.delete_item(14)
mycdll.delete_item(15)



print("After Deletion")

mycdll.return_elements()

