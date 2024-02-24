
# Node Class
# https://csuglobal.instructure.com/courses/87885/external_tools/51766
class Node: 
	def __init__(self, key): 
		self.key = key 
		self.left = None 
		self.right = None
		
# Tree Class
# https://youtu.be/KGkZH_cge9Q?feature=shared
class Tree:
    def __init__(self):
        self.root = []
    
    def build_tree(list):
        for current_node in list:
            while current_node is not None: 
                if Node.key < current_node.key:
                    # If there is no left child, add the new
                    # Node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = Node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # Node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = Node
                        current_node = None
                    else:
                        current_node = current_node.right
            else:
                current_node = self.root
                while current_node is not None: 
                    if Node.key < current_node.key:
                        # If there is no left child, add the new
                        # Node here; otherwise repeat from the
                        # left child.
                        if current_node.left is None:
                            current_node.left = Node
                            current_node = None
                        else:
                            current_node = current_node.left
                    else:
                        # If there is no right child, add the new
                        # Node here; otherwise repeat from the
                        # right child.
                        if current_node.right is None:
                            current_node.right = Node
                            current_node = None
                        else:
                            current_node = current_node.right
            return list.root
    
    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the Node if the key matches.
            if current_node.key == desired_key:
                return current_node
                
            # Navigate to the left if the search key is
            # less than the Node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
                
            # Navigate to the right if the search key is
            # greater than the Node's key.
            else:
                current_node = current_node.right
  
        # The key was not found in the tree.
        return None

    def insert(self, Node):
        # Check if the tree is empty
        if self.root is None:
            self.root = Node
        else:
            current_node = self.root
            while current_node is not None: 
                if Node.key < current_node.key:
                    # If there is no left child, add the new
                    # Node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = Node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # Node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = Node
                        current_node = None
                    else:
                        current_node = current_node.right

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