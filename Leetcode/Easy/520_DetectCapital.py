#%%

class Solution(object):
    def detectCapitalUseSlow(self, word):
        first_char = word[0]
        rest = word[1:]
        if first_char.isupper():
            return (rest.isupper() or rest.islower()) if len(rest)>0 else True
        else:
            return rest.islower() if len(rest)>0 else True
        
    def detectCapitalUse(self, word):
        first_char = word[0]
        starts_with_cap = False
        num_cap = 0
        
        if first_char.isupper():
            starts_with_cap = True
            num_cap = 1
            
        for c in word[1:]:
            if(ord(c)-ord('Z') <= 0 ):
                num_cap = num_cap + 1
        
        return num_cap ==0 or (starts_with_cap and (num_cap==1 or num_cap==len(word))) 
        
        
if __name__ == "__main__":
    s = Solution()
    
    data = [ ["USA", True],
             ["FLaG", False],
             ["A", True],
             ["a", True],
             ["Leetcode", True]
           ]
    
    for inp, outp in data:
        print("PASS" if s.detectCapitalUse(inp) == outp else "FAIL")


#%%