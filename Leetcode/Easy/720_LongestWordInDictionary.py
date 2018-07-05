#%%
class Solution(object):
    def longestWord(self, words, debug=False):
        words.sort()
        words.sort(key=len)

        q = []
        result = ""
        for i in range(len(words)):
            if len(words[i]) == 1:
                q.append(words[i])
                if result == "":
                    result = words[i]
            else:
                break
        
        remaining_words = set(words[i:])
        
        while len(q) > 0 :
            current_size = len(q)
            
            # traversing the current level
            for i in range(current_size):
                q_word = q.pop(0)
                
                # next possible word using q_word
                for new_ch in 'abcdefghijklmnopqrstuvwxyz':
                    temp = q_word + new_ch
                    if temp in remaining_words:
                        remaining_words.remove(temp)
                        q.append(temp)
                        if len(temp) > len(result):
                            result = temp
            
        return result


if __name__ == "__main__":
    S = Solution()
    
    data = [(["w","wo","wor","worl", "world"], "world"),
            (["a", "banana", "app", "appl", "ap", "apply", "apple", "appla"], "appla"),
            (["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"], "latte"),
            (["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"], "e")
            ]
    
    for inp, out in data:
        print(S.longestWord(inp, True) == out)
    
    
    
#%%