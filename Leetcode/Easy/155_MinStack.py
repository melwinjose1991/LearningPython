#%% 

class MinStack(object):

    def __init__(self):
        self.list = []
        self.min = -1
        
    def push(self, x):
        if len(self.list) == 0 or x < self.min:
            self.min = x
        
        self.list.append(self.min)
        self.list.append(x)
        
    def pop(self):
        if len(self.list) > 0 :
            top_element = self.list.pop()
            self.list.pop()
        
            if self.min == top_element and len(self.list) > 0:
                self.min = self.list[-2]
            
    def top(self):
        return None if len(self.list)==0 else self.list[-1]

    def getMin(self):
        return None if len(self.list)==0 else self.min
    

if __name__ == "__main__":
    minStack = MinStack()
    
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
   
    
    
#%%