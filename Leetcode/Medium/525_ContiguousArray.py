#%%

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_index_map = {0:-1}
        cur_sum = 0
        max_len = 0
        
        for i,num in enumerate(nums):
            if num == 1:
                cur_sum = cur_sum + 1
            else:
                cur_sum = cur_sum - 1
            
            if cur_sum in sum_index_map:
                cur_len = i - sum_index_map[cur_sum]
                if cur_len > max_len:
                    max_len = cur_len 
            else:
                sum_index_map[cur_sum] = i
                    
        # print(sum_index_map)
        
        return max_len
                
                
if __name__ == "__main__":
    s = Solution()
    
    data = [[[0,1], 2],
            [[0,1,0], 2],
            [[1,1,0,1,0,1,1], 4],
            [[0,1,0,1], 4]
            ]

    for inp, outp in data:
        print("PASS" if s.findMaxLength(inp) == outp else "FAIL")
                
#%%