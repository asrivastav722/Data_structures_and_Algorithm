class PQ:
    def __init__(self,list=None):
        self.list=[]
        print("Priority Queue is initialized")
    
    def push(self,data=None,priority=None):
        self.data=data
        self.priority=priority
        if len(self.list)==0:
            self.list.append([self.data,self.priority])
        else:
            if self.list[len(self.list)-1][1] <= self.priority:
                self.list.append([self.data,self.priority])
            else:
                index=0
                while index <= (len(self.list)-1):
                    if self.priority<self.list[index][1]:
                        self.list.insert(index,[self.data,self.priority])
                        break
                    elif self.priority==self.list[index][1]:
                        self.list.insert(index,[self.data,self.priority])
                        break
                    index=index+1
        
        print(self.data,"Pushed")

    def pop_item(self):
        temp=self.list[0]
        self.list.pop(0)
        print(temp[0],"Popped")
        return temp[0]
    
    def is_empty(self):
        if len(self.list)==0:
            print("Empty")
            return True
        else:
            print("Not Empty")
            return False

    def size(self):
        print(len(self.list))
        return len(self.list)

    
mypq=PQ()
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
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()
mypq.pop_item()

mypq.is_empty()
mypq.size()
