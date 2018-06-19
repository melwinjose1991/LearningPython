#%%

class Solution(object):
    def moveZeroes(self, nums):
        write_index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[write_index] = nums[i]
                write_index += 1
            
        for i in range(write_index, len(nums)) :
            nums[i] = 0


X = [[0, 1, 0, 2, 3, 0, 5, 0],
     [0, 0, 0],
     [0, 1, 0],
     [1, 2, 3],
     [1, 0, 1]]

for x in X:
    Solution().moveZeroes(x)
    print(x)


#%%