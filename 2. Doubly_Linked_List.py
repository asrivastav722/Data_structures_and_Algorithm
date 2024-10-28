class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    
    # Check if List is Empty or not
    def is_empty(self):
        if self.start is None:
            return "Empty"
        else:
            return "Not_Empty"
    
    #Search for an Element in the List
    def search(self,data):
        self.data=data
        temp=self.start
        count=0
        while temp is not None:
            if temp.item == self.data:
                count=1
                break
            else:
                count=0
            temp=temp.next
        if count == 1:
            return "Present"
        else:
            return "Not Present"
    
    #return Elements
    def return_elements(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next

    # Insert Element at Start
    def insert_at_start(self,data):
        self.data=data
        newNode=Node(None,self.data,None)
        if self.start is None:
            self.start=newNode
            self.start.prev=None
        else:
            self.start.prev=newNode
            newNode.next=self.start
            self.start.prev=None
            self.start=newNode
        
    # Insert Element at Last
    def insert_at_last(self,data):
        self.data=data
        newNode=Node(None,self.data,None)
        if self.start is None:
            self.start=newNode
        else:
            temp=self.start
            while temp is not None:
                if temp.next==None:
                    newNode.prev=temp
                    temp.next=newNode
                    break
                temp=temp.next

    # Insert Element after
    def insert_after(self,data,after):
        self.data=data
        self.after=after
        newNode=Node(None,self.data,None)
        temp=self.start
        while temp is not None:
            if temp.item == self.after:
                if temp.next is None:
                    newNode.next=temp.next
                    newNode.prev=temp
                    temp.next=newNode
                    break
                else:
                    temp.next.prev=newNode
                    newNode.next=temp.next
                    newNode.prev=temp
                    temp.next=newNode
                    break
            temp=temp.next
    
    #Insert Element before
    def insert_before(self,data,before):
        self.data=data
        self.before=before
        newNode=Node(None,self.data,Node)
        temp=self.start
        while temp is not None:
            if temp.item == self.before:
                if temp.prev is None:
                    newNode.next=temp
                    temp.prev=newNode
                    self.start=newNode
                    break
                else:
                    temp.prev.next=newNode
                    newNode.prev=temp.prev
                    newNode.next=temp
                    temp.prev=newNode
                    break
            temp=temp.next
               
    #Deletion
    #Delete First Element
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            self.start.prev=None
        else:
            return "no element at start"
            
    #Delete last Element
    def delete_last(self):
        temp=self.start
        if temp is None:
            pass
        elif temp.next is None:
            self.start=None
        else:
            while temp is not None:
                if temp.next is None:
                    temp.prev.next=None
                temp=temp.next
    
    #Delete Selected Element
    def delete_item(self,data):
        temp=self.start
        self.data=data
        while temp is not None:
            if temp.item==self.data:
                #If only Single Element is present in the List
                if temp.prev is None and temp.next is None:
                    self.start=None
                    return "The List is Empty Now"
                    break
                #If the Element is at the Start
                elif temp.prev is None:
                    self.start=temp.next
                    break
                #If the Element is at the End
                elif temp.next is None:
                    temp.prev.next=None
                    break
                #For Other Cases
                else:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    break              
            temp=temp.next
                



            
        

        





    

    

mydll=DLL()
mydll.insert_at_start(6)
mydll.insert_at_start(5)
mydll.insert_at_start(4)
mydll.insert_at_start(3)
mydll.insert_at_start(2)
mydll.insert_at_start(1)
print("Before")
mydll.return_elements()


print("After")
mydll.return_elements()





    