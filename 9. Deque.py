class DEQUE:
    def __init__(self,list=None):
        self.list=[]
        print("Deque is Initialized")

    def is_empty(self):
        if len(self.list)==0:
            print("The Deque is Empty")
            return True
        else:
            print("The Deque is not Empty")
            return False
    
    def size(self):
        print("Total Elements",len(self.list))
        return len(self.list)

    def insert_rear(self,data):
        self.data=data
        self.list.insert(0,self.data)
        print(self.data,"Inserted at Rear")
    
    def insert_front(self,data):
        self.data=data
        self.list.insert(len(self.list),data)
        print(self.data,"Inserted at front")
    
    def delete_rear(self):
        value=self.list.pop(0)
        print(value,"Deleted from rear")

    def delete_front(self):
        value=self.list.pop(-1)
        print(value,"Deleted from front")

    def print_list(self):
        print(self.list)

mydeque=DEQUE()

mydeque.insert_front(5)
mydeque.insert_front(1)
mydeque.insert_front(5)
mydeque.insert_front(3)
mydeque.insert_front(4)
mydeque.insert_front(0)
mydeque.insert_rear(40)
mydeque.print_list()
mydeque.delete_front()
mydeque.delete_front()
mydeque.delete_rear()
mydeque.delete_rear()
mydeque.print_list()