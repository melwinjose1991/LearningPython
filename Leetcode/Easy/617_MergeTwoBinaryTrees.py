#%%

class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        
        T = TreeNode(0)
        T.val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
        T.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        T.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return T
    
if __name__ == "__main__":
    T1 = TreeNode(1)
    T1_left = TreeNode(1)
    T1.left = T1_left
    
    T2 = TreeNode(1)
    T2_right = TreeNode(2)
    T2.right = T2_right
    
    T = Solution().mergeTrees(T1, T2)
    
#%%
    