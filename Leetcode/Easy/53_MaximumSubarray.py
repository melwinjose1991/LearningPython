#%% 53 - Maximum Subarray

'''

    Techinque : Linear DP - start / continue series.
        At every point you have an option of starting a new series or continuing
        the previous series. 
            
            For starting a new series, the value of current element should be 
            greater than the best series before it. 
            
            For continuing the current series, the current value of the element
            can be added the best series before it, this creates a new best 
            series.
            
'''

class Solution(object):
    def maxSubArray(self, nums):
        
        # dp[i-1] stores the maximum sum that includes the (i-1)th element as 
        # the last element. This can just the (i-1)th element or terms including
        # before that i.e i-2, i-3 ...
        dp = []
        
        dp.append(nums[0])
        max_sum = nums[0]

        for i in range(1,len(nums)):
            cur_element = nums[i]
            sum_including_last_element = dp[i-1] + cur_element
            
            # print("comparing ", cur_element, "&", sum_including_last_element)
            if cur_element > sum_including_last_element:
                dp.append(cur_element)
            else:
                dp.append(sum_including_last_element)
                
            max_sum = max(max_sum, dp[i])
    
        # print(dp) 
        # print(max_sum)
        return max_sum


if __name__ == "__main__":               
    S = Solution()
    
    cases = ( ([-2,1,-3,4,-1,2,1,-5,4], 6),
              ([1,2,3], 6),
              ([-1,-2,-3], -1),
              ([-3,-2,-1], -1),
              ([-1, 0, 1], 1),
              ([-1, -2, 0], 0)
            )
    
    for inp,out in cases:
        print(S.maxSubArray(inp) == out)
    
    

#%%