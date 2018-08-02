#%%

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = self.getMap(s)

        for c in t:
            if c in char_map:
                char_map[c] = char_map[c] - 1
                if char_map[c] == 0:
                    del char_map[c]
            else:
                return False
    
        return True if len(char_map) == 0 else False

    def getMap(self, str_in):
        char_map = {}
        for c in str_in:
            if c in char_map:
                char_map[c] = char_map[c] + 1
            else:
                char_map[c] = 1
        return char_map


if __name__ == "__main__":
    s = Solution()
    
    data = [["anagram","nagaram",True],
            ["rat","car", False]]
    
    for str1, str2, result in data:
        print("PASS" if s.isAnagram(str1, str2) == result else "FAIL" )
        


#%%