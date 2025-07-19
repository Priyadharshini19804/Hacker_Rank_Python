"""

Complete the preorder function in the editor below, which has 1 parameter: a pointer to the root of a binary tree. 
It must print the values in the tree's preorder traversal as a single line of space-separated values.

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  

Sample Output

1 2 5 3 4 6 

"""

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)


def preOrder(root):
    if root != None:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')

                    



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
