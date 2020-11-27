class Node:
    def __init__(self,val):
        self.next=None
        self.value=val

    def insert(self,val):
        if self.value:
            
            if self.next is None:
                self.next=Node(val)
            else:
                self.next.insert(val)
        else:
            self.value=val           

    def print_ll(self):
        if self.value:
            while self.next!= None:
                print(self.value)
                self=self.next
            print(self.value)
        else:
            print("LL is empty")

    def delete(self,val):
        i=0
        while self.value!=val and self.next!=None:
            i+=1
            self=self.next
        if self.next!=None:
            
            print("position is ",i)#find the index of value
            self=n1                 
            for j in range(0,i-1):  #travel to the node before it
                self=self.next
            k=self                  #Store the previous position in a variable
            l=self
            k=k.next.next           #take another variable and store the next value of the element to be deleted
            l.next=k
            '''Eliminate the current node by pointing the next value of the previous node to the next value of
               the element to be deleted'''
        else:
            print("Element Not found")
        
        
   
n1=Node(5)
n1.insert(12)
n1.insert(4)
n1.insert(6)
n1.insert(15)
print("Before deleting")
n1.print_ll()
n1.delete(6)
print("After deleting")
n1.print_ll()

n1.delete(163)
        

    
