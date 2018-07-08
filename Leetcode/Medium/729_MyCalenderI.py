#%%

class MyCalendar(object):

    def __init__(self):
        # each element is [start, end]
        self.events = []

    def book(self, start, end):
            # self.events.sort()
            for i_start,i_end in self.events:
                if start < i_end:
                    if end <= i_start:
                        continue
                    else:
                        return False
            
            self.events.append([start, end])
            return True

# In JAVA, TreeSet can be used to improve the algorithm even further    
    
if __name__ == "__main__":
    calender = MyCalendar()
    print(calender.book(10, 20))    
    print(calender.book(15, 25))    
    print(calender.book(20, 30))    
    print(calender.book(5, 15))
    print(calender.book(5, 10))        


#%%