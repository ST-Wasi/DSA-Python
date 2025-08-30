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



# Singly Linked List Implimenation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked List is Empty ")
            return
        while temp != None:
            print(temp.data,end=" --> ")
            temp = temp.next
        print("None")
    
    def search(self,target):
        if self.head == None:
            print ("Linked List Is Empty")
            return
        temp = self.head
        while(temp != None):
            if(temp.data == target):
                return True
            temp = temp.next
        return False
    
    def get_tail(self):
        if self.head == None:
            return None
        temp = self.head
        while temp.next != None:
            temp = temp.next
        return temp.data

    def insert_at_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def has_cycle(self):
        visited = set()
        temp = self.head
        while temp != None:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False
    

LL = LinkedList()

LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
LL.insert(45)

LL.display()
LL.insert_at_front(15)
LL.display()
LL.reverse()
LL.display()