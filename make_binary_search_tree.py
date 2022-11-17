class Node:
    def __init__(self, data, children, parent = None):
        self.data = data
        self.children = children
        self.parent = parent
    def __repr__(self):
        return f"<Node {self.data}>"


def make_root(data_list):
    if len(data_list) == 0:
        return None
    if len(data_list) == 1:
        return Node(data_list[0],[])

    idx = len(data_list) // 2
    left = data_list[:idx]
    right = data_list[idx+1:]
    root = Node(data_list[idx], [make_root(left), make_root(right)])
    while None in root.children:
        root.children.remove(None)
    return root


def add_parents(root_node):
    for child in root_node.children:
        child.parent = root_node
        if child.children:
            add_parents(child)

letter_list = [char for char in 'abcdefghijklmnopqrstuvwxyz']
root = make_root(letter_list)
add_parents(root)