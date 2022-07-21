class Stack:

    def __init__(self):
        self.pointer = -1
        self.list = [None for _ in range(2)]
    
    def append(self, element):        
        if self.pointer < len(self.list) - 1:
            self.list[self.pointer + 1] = element
            self.pointer += 1
        else:
            new_list = [None for _ in range(2*len(self.list))]
            for i in range(len(self.list)):
                new_list[i] = self.list[i]
            self.pointer = len(self.list)
            self.list = new_list
            self.list[self.pointer] = element    

    def isempty(self):
        return self.pointer < 0
    
    def pop(self):
        if not self.isempty():
            self.pointer -= 1
            return self.list[self.pointer + 1]
        else:
            print("Error: the stack is empty")
    
    def peek(self):
        if not self.isempty():
            return self.list[self.pointer]
        else:
            print("Error: the stack is empty")            