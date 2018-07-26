#%% 390 - Elimination Game
#           Binary Search with tracking head           

class Solution(object):
    def lastRemaining(self, n):
        left = True
        remaining = n
        step = 1
        head = 1
        
        while remaining > 1 :
            if left or (remaining%2)==1 :
                head = head + step
            
            remaining = int(remaining / 2)
            step = step * 2
            left = not left
            # print(head, remaining)
            
        return head

    

if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining(2))
    print(s.lastRemaining(4))    
    print(s.lastRemaining(6))
    print(s.lastRemaining(8))
    print(s.lastRemaining(9))

#%%