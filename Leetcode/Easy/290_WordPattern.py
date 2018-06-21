#%%
class Solution(object):
    
    def wordPattern(self, pattern, str):
        
        words = str.split()
        if len(words) != len(pattern):
            return False
              
        map_ch_word = {}
        map_word_ch = {}
            
        for ch,word in zip(pattern, words):
            if ch in map_ch_word:
                if word not in map_word_ch or map_word_ch[word] != ch or \
                    map_ch_word[ch] != word:
                    return False
            else:
                if word in map_word_ch:
                    return False
                
                map_ch_word[ch] = word
                map_word_ch[word] = ch
        
        return True



if __name__ == "__main__":
    args = [['abba', 'dog cat cat dog', True],
            ['abba', 'dog cat cat fish', False],
            ['aaaa', 'dog cat cat dog', False],
            ['abba', 'dog dog dog dog', False]
            ]
    
    s = Solution()
    
    for pattern, string, expected in args:
        result = s.wordPattern(pattern, string)
        assert result==expected, "Wrong Answer"



#%%