#%% 

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        cur_node = head
        while cur_node:
            tmp = cur_node.next
            while tmp and tmp.val == cur_node.val:
                tmp = tmp.next
            cur_node.next = tmp
            cur_node = tmp
        
        return head


def createLinkedList(nums):
    if nums is None or len(nums)==0:
        return None
    
    head = None
    prev = None
    for num in nums:
        if head is None:
            head = ListNode(num)
            prev = head
        else:
            new_node=  ListNode(num)
            prev.next = new_node
            prev = new_node
            
    return head

def printLinkedList(node):
    while node:
        print(node.val)
        node = node.next
    print()

if __name__ == "__main__":
    lists = [[1,1,2],
             [1,1,2,3,3],
             [],
             None,
             [1,2,3],
             [1,1,1],
             [1,1,2,3],
             [1,2,3,3]
             ]
    
    s = Solution()
    
    for l in lists:
        list_obj = createLinkedList(l)
        printLinkedList(s.deleteDuplicates(list_obj))

#%%