from re import L


class stack:
    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def push(self,data):
        self.data.append(data)     

    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return(self.data.pop())
    
    def top(self):
        if self.is_empty():
            print("stack is Empty")
        else:
            return self.data[-1]


a = stack()
print(a.is_empty())
a.push(11)
a.push(10)
print(a.top())


def is_matched(expr):
    lefty = "([{"
    righty = ")]}"
    s = stack( )
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty( ):
                return False
            if righty.index(c) != lefty.index(s.pop( )):
                return False
    return s.is_empty( )            



print(is_matched('{{}})'))