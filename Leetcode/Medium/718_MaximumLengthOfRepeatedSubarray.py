#%%

#   LCS Style DP - used when subsequence / subarray of two array needs to be
#                  evaluated. Returns some function of the two i.e max length .

class Solution(object):
    def findLength(self, A, B):
        
        DP = []
        ret = 0
        
        for i in range(len(A)):
            tmp = []
            for j in range(len(B)):
                if i==0 or j==0:
                    if A[i] == B[j]:
                        tmp.append(1)
                    else:
                        tmp.append(0)
                else:
                    if A[i] == B[j]:
                        tmp.append(DP[i-1][j-1]+1)
                    else:
                        tmp.append(0)
            
            ret = max(ret, max(tmp))
            DP.append(tmp)
            
        return ret



if __name__ == "__main__":
    S = Solution()
    print(S.findLength([1,2,3,2,1],[3,2,1,4,7]))
    print(S.findLength([1,2,1],[2,1,0]))
    
    
#%%