class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    #Create a dictionary
    d = {}
    
    # create a function for traversing
    def traverse(root, key, level):
        if root:
            if key not in d:
                d[key]=[root, level]
            elif d[key][1] > level:
                d[key] = [root, level]
                
            #traverse left and right of tree
            traverse(root.left, key-1, level+1)
            traverse(root.right, key+1, level+1)
    traverse(root, 0, 0)
    
    for key in sorted(d):
        print(d[key][0], end=" ")



HackerRank: https://www.hackerrank.com/challenges/tree-top-view/problem
GeeksForGeeks: https://www.youtube.com/watch?v=KXfok9IiVHQ&list=PLqM7alHXFySHCXD7r1J0ky9Zg_GBB1dbk&index=17
