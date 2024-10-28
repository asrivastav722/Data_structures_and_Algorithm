class Node:
    def __init__ (self,item=None,next=None):
        self.item=item
        self.next=next

class pqueue:
    def __init__(self,start=None):
        self.start=start
    
    def push(self,data,priority):
        self.priority=priority
        self.data=data
        if self.start is None:
            self.start=Node([self.data,self.priority],None)
        elif self.start.next is None:
            if self.priority<= self.start.item[1]:
                self.start=Node([self.data,self.priority],self.start)
            else:
                self.start.next=Node([self.data,self.priority],None)
        else:
            last=self.start
            while last.next is not None:
                last=last.next
            if last.item[1]<=self.priority:
                last.next=Node([self.data,self.priority],None)
            else:
                if self.start.item[1]>= self.priority:
                    self.start=Node([self.data,self.priority],self.start)
                else: 
                    temp=self.start
                    while temp is not None:
                        if temp.next is None:
                            break
                        elif self.priority<=temp.next.item[1]:
                            temp.next=Node([self.data,self.priority],temp.next)
                            break
                        temp=temp.next
        print(self.data,"Pushed")

    def pop(self):
        if self.start is not None:
            value=self.start.item[0]
            print(value,"Popped")
            self.start=self.start.next
            return value  
    
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next

mypq=pqueue()
mypq.push("i",8)
mypq.push("h",7)
mypq.push("g",6)
mypq.push("f",5)
mypq.push("e",4)
mypq.push("d",3)
mypq.push("c",2)
mypq.push("b",1)
mypq.push("a",0)
mypq.push("j",9)
mypq.push("k",10)
mypq.push("l",11)
mypq.push("n",16)
mypq.push("o",99)
mypq.push("m",14)
print("---------------")
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.pop()
mypq.print_all()
