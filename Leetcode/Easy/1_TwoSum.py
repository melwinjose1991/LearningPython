#%%
class Solution(object):
    def twoSum(self, nums, target):
        map_num_index = {}
        for i,num in enumerate(nums):
            if target - num in map_num_index:
                return [map_num_index[target-num], i]
            
            map_num_index[num] = i
        
        
if __name__ == "__main__":
    S = Solution()
    
    data = [([2,7,11,15],9,[0,1])]
    
    for (inp, target, out) in data:
        print( S.twoSum(inp, target) == out )



#%%