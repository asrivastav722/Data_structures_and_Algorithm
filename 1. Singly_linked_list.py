class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class SLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        if self.start is None:
            return "true"
        else:
            retrun "false"
            
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next
            
    def insert_at_start(self,data=None,next=None):
        self.data=data
        n=Node(self.data)
        n.next=self.start
        self.start=n
    
    def insert_at_last(self,data=None):
        self.data=data
        n=Node(self.data)
        temp=self.start
        while temp is not None:
            if temp.next is None:
                temp.next=n
                break
            temp=temp.next
    
    def insert_after(self,data=None,after=None):
        self.data=data
        self.after=after
        n=Node(self.data)
        temp=self.start
        while temp is not None:
            if temp.item==self.after:
                n.next=temp.next
                temp.next=n
                break
            temp=temp.next
    
    def delete_first(self):
        self.start=self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.item is not None:
                if temp.next.next is None:
                    temp.next=None
                    break
                temp=temp.next
    
    def delete_item(self,data=None):
        self.data=data
        if self.start is None:
            pass         
        elif self.start.item == self.data:
            self.start=self.start.next
        else:
            temp=self.start
            while temp is not None:
                if temp.next.item == self.data:
                    temp.next=temp.next.next
                    break
                temp=temp.next
    
    def search(self,data):
        self.data=data
        temp=self.start
        avail=0
        while temp is not None:
            if temp.item==self.data:
                avail=1
                break
            temp=temp.next
        if avail==1:
            print("true")
        else:
            print("false")

    def length(self):
        temp=self.start
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        return count
    
    def remove_duplicate(self):
            
        
        
           
mysll=SLL()
mysll.insert_at_start(5)
mysll.insert_at_start(6)
mysll.insert_at_start(7)
mysll.insert_at_start(8)
mysll.insert_at_start(8)
mysll.insert_at_start(9)
mysll.insert_at_start(10)
mysll.insert_at_start(11)
mysll.insert_at_start(11)
mysll.remove_duplicate()





    
