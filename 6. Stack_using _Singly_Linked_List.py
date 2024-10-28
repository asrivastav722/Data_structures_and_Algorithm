class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class Stack:
    def __init__(self,start=None):
        self.start=start
        print("Stack Initialized")

    def push(self,data):
        self.data=data
        newNode=Node(self.data,self.start)
        self.start=newNode
        print (self.data,"Pushed")
    
    def pop(self):
        if self.start is None:
            print("Stack is empty")
        else:
            value=self.start.item
            self.start=self.start.next
            print(value,"Popped")
           
    

mystack=Stack()
mystack.push(5)
mystack.push(10)
mystack.push(11)
mystack.push(12)
mystack.push(13)
mystack.pop()
mystack.pop()
mystack.pop()
mystack.pop()
mystack.pop()
mystack.pop()
