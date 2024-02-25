# https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
class Node(object):
	def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.height = 0

# https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python
class Tree(object):
    def __init__(self):
        super(Tree, self).__init__()
        self.root = None
        self.size = 0

    def buildTree(nums):
        if not nums:
            return None
        # https://www.trainingint.com/how-to-find-duplicates-in-a-python-list.html
        # I chose this solution because I wanted to remove duplicates but maintain the pseudorandom
        # nature of the generated numbers to ensure a more balanced BST
        nums = list(set(nums))
        root = Node(nums[0])
        q = [root]
        i = 1
        while i < len(nums):
            curr = q.pop(0)
            if i < len(nums):
                curr.left = Node(nums[i])
                q.append(curr.left)
                i += 1
            if i < len(nums):
                curr.right = Node(nums[i])
                q.append(curr.right)
                i += 1
        return root # Unclear whether or not this meets the intent of the assignment referencing
                    # returning the "level-1 root node"

    def printTree(root):
        if not root:
            return
        printTree(root.left)
        print(root.val, end=" ")
        printTree(root.right)

    # https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/
    def maxDepth(node):
        if node is None:
            return 0
        else:
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
            
    # https://www.geeksforgeeks.org/insertion-in-binary-search-tree/
    def insert(root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root
    
    # https://www.geeksforgeeks.org/deletion-in-binary-search-tree/
    def delete(root, key):
        # Base case
        if root is None:
            return root
    
        # Recursive calls for ancestors of
        # node to be deleted
        if root.val > key:
            root.left = delete(root.left, key)
            return root
        elif root.val < key:
            root.right = delete(root.right, key)
            return root
    
        # We reach here when root is the node
        # to be deleted.
    
        # If one of the children is empty
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
    
        # If both children exist
        else:
    
            succParent = root
    
            # Find successor
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
    
            # Delete successor.  Since successor
            # is always left child of its parent
            # we can safely make successor's right
            # right child as left of its parent.
            # If there is no succ, then assign
            # succ.right to succParent.right
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
    
            # Copy Successor Data to root
            root.val = succ.val
    
            # Delete Successor and return root
            del succ
            return root

# Second definition required for Tree class to recognize existence of following functions
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)

def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

# https://www.geeksforgeeks.org/insertion-in-binary-search-tree/
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# https://www.geeksforgeeks.org/deletion-in-binary-search-tree/
def delete(root, key):
    # Base case
    if root is None:
        return root
 
    # Recursive calls for ancestors of
    # node to be deleted
    if root.val > key:
        root.left = delete(root.left, key)
        return root
    elif root.val < key:
        root.right = delete(root.right, key)
        return root
 
    # We reach here when root is the node
    # to be deleted.
 
    # If one of the children is empty
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
 
    # If both children exist
    else:
 
        succParent = root
 
        # Find successor
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
 
        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
 
        # Copy Successor Data to root
        root.val = succ.val
 
        # Delete Successor and return root
        del succ
        return root