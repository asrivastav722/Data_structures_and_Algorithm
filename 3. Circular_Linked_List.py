class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last
    
    #Insertion
    #Insert at Start
    def insert_at_start(self,data):
        self.data=data
        newNode=Node(self.data,None)
        if self.last is None:
            self.last=newNode
        elif self.last.next is None:
            self.last.next=newNode
            newNode.next=self.last
        else:            
            newNode.next=self.last.next
            self.last.next=newNode

    #Insert at Last
    def insert_at_last(self,data):
        self.data=data
        newNode=Node(self.data,None)
        if self.last is None:
            self.last=newNode
        elif self.last.next is None:
            newNode.next=self.last
            self.last.next=newNode
            self.last=newNode
        else:
            newNode.next=self.last.next
            self.last.next=newNode
            self.last=newNode
    
    #Insert after
    def insert_after(self,after,data):
        self.data=data
        self.after=after
        newNode=Node(self.data,None)
        if self.after == self.last.item: 
            if self.last.next is None:
                newNode.next=self.last
                self.last.next=newNode
                self.last=newNode
            else:
                newNode.next=self.last.next
                self.last.next=newNode
                self.last=newNode
        elif self.after == self.last.next.item:
            newNode.next=self.last.next.next
            self.last.next.next=newNode
        else:
            temp=self.last.next
            while temp != self.last:
                if self.after == temp.item:
                    newNode.next=temp.next
                    temp.next=newNode
                    break
                temp=temp.next

    #Insert Before
    def insert_before(self,before,data):
        self.data=data
        self.before=before
        newNode=Node(self.data,None)
        if self.before is self.last.item:
            if self.last.next is None:
                newNode.next=self.last
                newNode.next.next=newNode
                self.last=newNode
            elif self.last.next is not None:
                newNode.next=self.last
                start=self.last.next
                while start is not self.last:
                    temp=start
                    start=start.next
                temp.next=newNode
        elif self.last.next.item is self.before:
            newNode.next=self.last.next
            self.last.next=newNode
        else:
            pos=self.last
            while pos.next.item is not self.last:
                if pos.next.item == self.before:
                    newNode.next=pos.next
                    pos.next=newNode
                    break
                pos=pos.next
    
    # Deletion
    # Delete First Element
    def delete_first(self):
        if self.last is None:
            pass
        elif self.last.next is None:
            self.last=None
        elif self.last.next.next is self.last:
            self.last.next=None
        else:
            self.last.next=self.last.next.next

    # Delete Last Element 
    def delete_last(self):
        if self.last is None:
            pass
        elif self.last.next is None:
            self.last=None
        elif self.last.next.next is self.last:
            self.last=self.last.next.next
            self.last.next=None
        else:
            start=self.last.next.next
            while start is not self.last:
                lastSecond=start
                start=start.next
            lastSecond.next=self.last.next
            self.last=lastSecond

    
    
    # Delete Item 
    def delete_item(self,data):
        self.data=data
        if self.last is None:
            pass
        #If the item is at the last
        elif self.last.item is self.data:
            if self.last.next is self.last:
                    self.last=None
            elif self.last.next is None: 
                self.last=None
                print(self.last.item,"=data")
            else:
                if self.last.next.next is self.last:
                    self.last=self.last.next
                    self.last.next=None
                
                else:
                    start=self.last.next.next
                    while start is not self.last:
                        lastSecond=start
                        start=start.next
                    lastSecond.next=self.last.next
                    self.last=lastSecond
        #if item is at start
        elif self.data is self.last.next.item:
            self.last.next=self.last.next.next            
        else:
            temp=self.last.next
            localization=temp
            while temp.item is not self.data:
                localization=temp
                temp=temp.next
            localization.next=localization.next.next

    #Return Elements
    def return_elements(self):
        if self.last is None:
            pass
        elif self.last.next is None:
            print(self.last.item)
        else:
            first=self.last.next
            while first != self.last:
                print(first.item)
                first=first.next
            print(self.last.item)


        
        



         
        
mycll=CLL()
mycll.insert_at_start(1)
mycll.insert_at_start(2)
mycll.insert_at_start(3)
mycll.insert_at_start(4)
mycll.insert_at_start(5)
mycll.insert_at_start(6)
mycll.insert_at_start(7)
mycll.insert_at_start(8)

mycll.return_elements()

mycll.delete_item(8)
mycll.delete_item(5)
mycll.delete_item(4)
mycll.delete_item(7)
mycll.delete_item(6)
mycll.delete_item(2)

mycll.delete_item(1)





print("after deletion")
mycll.return_elements()



