#%% 677 - Map Sum Pairs


class Node:
    def __init__(self):
        self.map = [None] * 27
    
    def hasChild(self, key):
        key_index = ord(key) - ord('a') + 1
        return self.map[key_index] != None
    
    def insertChild(self, key):
        key_index = ord(key) - ord('a') + 1
        self.map[key_index] = Node()
        
    def getChild(self, key):
        key_index = ord(key) - ord('a') + 1
        return self.map[key_index]

    
class MapSum(object):

    def __init__(self):
        self.root = Node()
        
    def insert(self, key, val):
        cur_node = self.root
        index = 0 
        
        while index < len(key):
            if not cur_node.hasChild(key[index]):
                cur_node.insertChild(key[index])
                
            cur_node = cur_node.getChild(key[index])
            index = index + 1
        
        cur_node.map[0] = val
        
    def sum(self, prefix):
        index = 0
        cur_node = self.root
        
        while index < len(prefix):
            if cur_node.hasChild(prefix[index]):
                cur_node = cur_node.getChild(prefix[index])
                index = index + 1
            else:
                return 0
        
        # print("sum :: ", cur_node.map.keys())
        return self.DFS(cur_node)

    def DFS(self, node):
        sum = 0
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if node.hasChild(ch):
                sum = sum + self.DFS(node.getChild(ch))

        return sum + (node.map[0] if node.map[0] != None else 0)
    
    
if __name__ == "__main__":
    ms = MapSum()
    
    ms.insert("apple", 3)
    print(ms.sum("ap"))
    
    ms.insert("app", 2)
    print(ms.sum("ab"))
    
    print(ms.sum("ap"))
    
    
    
#%%