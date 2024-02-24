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
        return root

    def printTree(root):
        if not root:
            return
        printTree(root.left)
        print(root.val, end=" ")
        printTree(root.right)

# Second definition required for Tree class to recognize existence of function
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)