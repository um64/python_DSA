

class singly:
    class node:
        def __init__(self,data):
            self.element = data
            self.next = None
    def __init__(self):
        self.head = None
        self.size = 0

    def traversal(self):
        if self.head is None:
            print("list is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.element)
                n = n.next

    def add_s(self,data):
        new = self.node(data)
        new.next = self.head
        self.head = new
        self.size +=1

    def add_end(self,data):
        new = self.node(data)
        if self.head is None:
            self.head = new
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new

    def delete(self):
        self.head.element = self.head.next
        self.size   -=1


s = singly()
list = [5,6,7]
for i in list:
    s.add_s(i)

s.add_s(99)    
s.add_end(1)
s.delete()
s.traversal()








                                      



