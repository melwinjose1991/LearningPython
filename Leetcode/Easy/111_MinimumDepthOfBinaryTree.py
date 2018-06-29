#%% 111 - Minimum Depth of Binary Tree

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        # Four Cases
        if left_depth == 0 and right_depth == 0:
            return min(left_depth, right_depth) + 1 
        
        if left_depth == 0:
            return right_depth + 1
        
        if right_depth == 0:
            return left_depth + 1
        
        return min(left_depth, right_depth) + 1
                

if __name__ == "__main__":
        root = TreeNode(3)
        root_left = TreeNode(9)
        root_right = TreeNode(20)
        
        root_right_left = TreeNode(15)
        root_right_right = TreeNode(7)
        root_right.left = root_right_left
        root_right.right = root_right_right
        
        root.left = root_left
        root.right = root_right
        
        print(Solution().minDepth(root))
    


#%%