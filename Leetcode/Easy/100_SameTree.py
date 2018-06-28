#%%

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        
        if  ( p is None and q is not None ) or \
            ( p is not None and q is None ) or \
            ( p.val != q.val ) :
                return False
        
        return ( self.isSameTree(p.left, q.left) and \
                 self.isSameTree(p.right, q.right) and \
                 p.val==q.val 
               )
        
        
if __name__ == "__main__": 
    t1 = TreeNode(1)
    t1_left = TreeNode(2)
    t1_right = TreeNode(3)
    t1.left = t1_left
    t1.right = t1_right
    
    t2 = TreeNode(1)
    t2_left = TreeNode(2)
    t2_right = TreeNode(3)
    t2.left = t2_left
    t2.right = t2_right
    
    s = Solution()
    print(s.isSameTree(t1, t2))
    
    

#%%