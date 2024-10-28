class Queue:
    def __init__(self,list=None):
        self.list=[]

    def size(self):
        print("Size=",len(self.list))
        return len(self.list)
    
    def enqueue(self,data):
        self.data=data
        self.list.insert(0,self.data)
        print(self.data,"Inserted")
    
    def dequeue(self):
        if len(self.list) == 0:
            print("Queue is Empty")
        else:
            temp=self.list[len(self.list)-1]
            self.list.remove(self.list[len(self.list)-1])
            print(temp,"Removed")
            return temp
    
    def get_rear(self):
        print("Rare =",self.list[0])
        return self.list[0]
    def get_front(self):
        print("Front =",self.list[len(self.list)-1])
        return self.list[len(self.list)-1]
    
    def is_empty(self):
        if len(self.list) ==0:
            print("Empty")
            return True
        else:
            print("Not Empty")
            return False

    

myqueue=Queue()
myqueue.enqueue(10)
myqueue.get_front()
myqueue.get_rear()
myqueue.is_empty()
myqueue.size()



        