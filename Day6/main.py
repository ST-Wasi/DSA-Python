# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def push(self,item):
#         self.items.append(item)
    
#     def pop(self):
#         if not self.is_empty():
#             self.items.pop()
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return None
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def display(self):
#         print(self.items[::-1])

# stack = Stack()

# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)
# stack.display()
# stack.pop()
# stack.display()
# print(stack.peek())



#Stack Implimentation with LIst

class Stack:
    def __init__(self):
        self.item = []
    
    def push(self,item):
        self.item.append(item)

    def pop(self):
        if not self.is_empty():
            self.item.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.item) == 0

    def display(self):
        print(self.item[::-1])

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
stack.pop()
stack.display()