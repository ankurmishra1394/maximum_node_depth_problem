class BinaryTree:

    def __init__(self, value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

max_node_depth = 1

def calculateDepthSum(root, mul_val, parent):
    if root is None:
        return

    global max_node_depth
    
    max_node_depth += (parent.value*mul_val)

    calculateDepthSum(root.left, mul_val=2, parent=root)
    calculateDepthSum(root.right, mul_val=3, parent=root)

def BinaryTreeNodeDepthSum(root):
    if root:
        calculateDepthSum(root.left, mul_val=2, parent=root)
        calculateDepthSum(root.right, mul_val=3, parent=root)
    return max_node_depth

def search(root, value):
    if not root:
        return None
    
    if root.value == value:
        return root
    
    found_node = search(root.left, value)
    if found_node:
        return found_node

    found_node = search(root.right, value)
    if found_node:
        return found_node

def print_tree(root, side="root"):
    if not root:
        return None

    print(side+" Node Value = "+str(root.value))
    print_tree(root.left, "left")
    print_tree(root.right, "right")

def generate_binart_tree(input_tree):
    root = BinaryTree(int(input_tree["tree"]["root"]))
    for each in input_tree["tree"]["nodes"]:
        node = search(root, int(each["value"]))
        if each["left"] is not None:
            node.left = BinaryTree(int(each["left"]))
        if each["right"] is not None:
            node.right = BinaryTree(int(each["right"]))
    return root

input_tree = {
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": None, "right": None, "value": 2},
      {"id": "3", "left": None, "right": None, "value": 3}
    ],
    "root": "1"
  }
}

root = generate_binart_tree(input_tree)
# print_tree(root)
BinaryTreeNodeDepthSum(root)
print("Maximum Nodes's Depth is {}".format(max_node_depth))