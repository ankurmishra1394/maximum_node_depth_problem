class BinaryTree:

    def __init__(self, value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

max_node_depth = 0

def BinaryTreeNodeDepthSum(root, current_depth=0):
    global max_node_depth
    if root is None:
        if current_depth > max_node_depth:
            max_node_depth = current_depth
            current_depth = 0
        return root
    elif root.left is None and root.right is None and current_depth == 0:
        return 0
    else:
        current_depth += root.value

    BinaryTreeNodeDepthSum(root.left, current_depth)
    BinaryTreeNodeDepthSum(root.right, current_depth)

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
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": None, "right": None, "value": 5},
      {"id": "6", "left": None, "right": None, "value": 6},
      {"id": "7", "left": None, "right": None, "value": 7},
      {"id": "8", "left": None, "right": None, "value": 8},
      {"id": "9", "left": None, "right": None, "value": 9}
    ],
    "root": "1"
  }
}



root = generate_binart_tree(input_tree)
# print_tree(root)
BinaryTreeNodeDepthSum(root)
print("Maximum Nodes's Depth is {}".format(max_node_depth))