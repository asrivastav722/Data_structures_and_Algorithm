class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class deque:
    def __init__(self,start=None):
        self.start=start
        print("The deque is initialized")
    
    def is_empty(self):
        if self.start is None:
            print("The Deque is empty")
            return True
        else:
            print("The deque is not Empty")
            return False
    
    def size(self):
        count=0
        temp=self.start
        while temp is not None:
            count=count+1
            temp=temp.next
        return count

    def insert_front(self,data):
        self.data=data
        self.start=Node(None,self.data,self.start)
    
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next
        
    def insert_last(self,data):
        self.data=data
        temp=self.start
        while self.start.next is not None:
            temp=temp.next
        temp.next=Node(temp,self.data,None)
    
        
            



        


mydeque=deque()
mydeque.insert_front(5)
mydeque.insert_front(10)
mydeque.insert_front(15)
mydeque.insert_front(20)
mydeque.print_all()
mydeque.delete_first()
mydeque.print_all()


            
