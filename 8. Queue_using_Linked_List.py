class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,start=None):
        self.start=start
        print("The Queue is Initialized")
    
    def is_empty(self):
        if self.start is None:
            print("The Queue is Empty")
            return True
            
        else:
            print("The Queue is not Empty")
            return False
            
    
    
    def enqueue(self,data):
        self.data=data
        if self.start is None:
            self.start=Node(self.data,None)
        else:
            temp=self.start
            while temp is not None:
                if temp.next is None:
                    temp.next=Node(self.data,None)
                    break
                temp=temp.next
        print(self.data,"Inserted")


    def dequeue(self):
        if self.start is None:
            pass
        else:
            value=self.start.item
            self.start=self.start.next
            print(value,"Removed")
            return value
    
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next

    def get_front(self):
        if self.start is None:
            pass
        else:
            print("Front=",self.start.item)
    
    def get_rear(self):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.next is None:
                    rear=temp.item
                temp=temp.next    
            print("Rear=",rear)
myqueue=Queue()
myqueue.is_empty()
myqueue.enqueue(5)
myqueue.enqueue(10)
myqueue.enqueue(20)
myqueue.enqueue(30)
myqueue.enqueue(40)
myqueue.dequeue()
myqueue.dequeue()
myqueue.get_front()
myqueue.get_rear()


        
