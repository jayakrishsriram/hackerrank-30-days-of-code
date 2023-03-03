import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self,root):
        #Write your code here
        n=list()
        n_t=''
        n.append(root)
        while len(n):
            node=n.pop(0)
            if node.left:
                n.append(node.left)
            if node.right:
                n.append(node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)                
            n_t+=str(node.data)+' '
        print(n_t)
