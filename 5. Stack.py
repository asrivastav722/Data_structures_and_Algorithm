class Stack:
    def __init__(self):
        self.list=[]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def push(self,data):
        self.data=data
        self.list.insert(0,self.data)
    
    def pop(self):
        if len(self.list)!=0:
            temp=self.list[0]
            self.list.remove(self.list[0])
            return temp
    
    def peek(self):
        return self.list[0]
            
    def size(self):
        return len(self.list)
    

mystack=Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
print(mystack.peek())
print(mystack.pop())
print(mystack.peek())

print(mystack.is_empty())
