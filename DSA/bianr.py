class binary:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):

        if data == self.data:
            pass

        

        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = binary(data)

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else: 
                self.left = binary(data)

    def search(self,data):

        if data == self.data:
            print("element found")            

        if data > self.data:
            if self.right:
                self.right.search(data)
            else: 
                print("data not found")    



        if data < self.data: 
            if self.left:
                self.left.search(data)
            else:
                print("data not found")



a = binary(4)
list = [1,3,57,111,6]
for item in list:
    a.insert(item)

for item in list:
    a.search(item)
