class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

    def insert(self,key):
        if self.value:
            if self.value>key:
                if self.left is None:
                    self.left=Node(key)
                else:
                    self.left.insert(key)
            if self.value<key:
                if self.right is None:
                    self.right=Node(key)
                else:
                    self.right.insert(key)
        else:
            self.value=key
    def inord(self):
        if self.left:
            self.left.inord()
        print(self.value)
        if self.right:
            self.right.inord()

root=Node(10)
root.insert(4)
root.insert(14)
root.insert(7)
root.inord()

        
        


    
            

        


    
            
                    
            
        

    
            
                
                    
    




        
    
