
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
    
    def build_tree(self):
          return level1
    
    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
                
            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
                
            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_node = current_node.right
  
        # The key was not found in the tree.
        return None

    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None: 
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right