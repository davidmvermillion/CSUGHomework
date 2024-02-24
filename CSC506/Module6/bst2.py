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


# https://csuglobal.instructure.com/courses/87885/external_tools/51766
def delete(self, key):
    parent = None
    current_node = self.root
    
    # Search for the Node.
    while current_node is not None:
    
        # Check if current_node has a matching key.
        if current_node.key == key: 
            if current_node.left is None and current_node.right is None:   # Case 1
                if parent is None: # Node is root
                    self.root = None
                elif parent.left is current_node: 
                    parent.left = None
                else:
                    parent.right = None
                return  # Node found and removed
            elif current_node.left is not None and current_node.right is None:  # Case 2
                if parent is None: # Node is root
                    self.root = current_node.left
                elif parent.left is current_node: 
                    parent.left = current_node.left
                else:
                    parent.right = current_node.left
                return  # Node found and removed
            elif current_node.left is None and current_node.right is not None:  # Case 2
                if parent is None: # Node is root
                    self.root = current_node.right
                elif parent.left is current_node:
                    parent.left = current_node.right
                else:
                    parent.right = current_node.right
                return  # Node found and removed
            else:                                    # Case 3
                # Find successor (leftmost child of right subtree)
                successor = current_node.right
                while successor.left is not None:
                    successor = successor.left
                current_node.key = successor.key      # Copy successor to current Node
                parent = current_node
                current_node = current_node.right     # Remove successor from right subtree
                key = parent.key                      # Loop continues with new key
        elif current_node.key < key: # Search right
            parent = current_node
            current_node = current_node.right
        else:                        # Search left
            parent = current_node
            current_node = current_node.left
            
    return # Node not found