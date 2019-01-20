#%%

class Solution(object):
    def combinationSum(self, candidates, target):
        self.result = []
        candidates = sorted(candidates)
        self.recursiveFunction(self.result, [], target, candidates, 0, 0)
        return self.result
        
    def recursiveFunction(self, sol_list, cur_list, target, candidates, index, depth):
        # tabs = '\t' * depth
        # print(tabs, cur_list)
        if target == 0 :
            sol_list.append(cur_list.copy())
            # print(tabs, "ADDED")
        else:
            for i in range(index, len(candidates)):
                no = candidates[i]
                # print(tabs, no, target, target-no, cur_list)
                if (target - no) >= 0 :
                    # print(tabs, "RECURSING")
                    cur_list.append(no)
                    self.recursiveFunction(sol_list, cur_list, (target-no), candidates, i, depth+1)
                    cur_list.pop()
                else:
                    return


if __name__ == "__main__":
    s = Solution()
    data = [ [[2,3,5], 8],
             [[2,3,6,7], 7]
            ]
    
    for inp, target in data:
        print(s.combinationSum(inp, target))


#%%