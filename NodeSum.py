import sys
import queue
sys.setrecursionlimit(10**6)


class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root
        
def sumOfAllNodes(root) :
    
    if root is None:
        return None
    sum = root.data
    for child in root.children:
        
        sum=sum+sumOfAllNodes(child) #no child.data because we can't iterate on integer
    return sum
    
 
    
    
li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(sumOfAllNodes(root))