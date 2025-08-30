from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(arr, index=[-1]):
    index[0] += 1
    if index[0] >= len(arr) or arr[index[0]] == -1:
        return None
    
    root  = Node(arr[index[0]])
    root.left = buildTree(arr,index)
    root.right = buildTree(arr,index)
    return root



    

def preorder(root): # Root ---> Left ----> Right
    if root != None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root): # Left ---> Root --> Right 
    if root != None:
        print(root.data, end=" ")
        inorder(root.left)
        inorder(root.right)

def postorder(root): # Left --> Right ---> Root
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = buildTree([12,7,17,3,9,14,-1])

# inorder(root)
# print("")
# preorder(root)

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height,right_height)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
# print("")
# print(count_nodes(root))

# d = deque([1,2,3,4,5,6,7,8,9])
# .append Will append the Elemet to the Right end of the Queue
# d.append(10)

# .appendleft() Will append the Elemet to the left end of the Queue
# d.appendleft(0)

# .pop() Will removing the Elemet to the right end of the Queue
# d.pop()

# .popleft() Will removing the Elemet to the Left end of the Queue
# d.popleft()



def bfs_or_level_order(root,level):
    if root is None:
        return
    
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        bfs_or_level_order(root.left,level-1)
        bfs_or_level_order(root.right,level-1)

def main_function():
    height_of_tree = height(root)

    total_level = height_of_tree + 1

    for level_num in  range(1, total_level):
        bfs_or_level_order(root,level_num)
        print()
 

# main_function()


def kth_largest_element(root,k):
    counter = [0]
    result = [None]
    def reverse_inorder(root):
        if not root or result[0] is not None:
            return
        reverse_inorder(root.right)

        counter[0] += 1
        if(counter[0] == k):
            result[0] = root.data
            return
        
        reverse_inorder(root.left)

    reverse_inorder(root)
    return result[0] if result[0] is not None else -10**9 # Int min

# print(kth_largest_element(root,2))
inorder(root)


# def reverse_inorder(root):
#     if not root:
#         return
#     reverse_inorder(root.right)

#     print(root.data)
        
#     reverse_inorder(root.left)

# reverse_inorder(root)
