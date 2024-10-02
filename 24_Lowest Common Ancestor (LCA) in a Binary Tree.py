class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None
    if root == p or root == q:
        return root
    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

def build_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def find_node(root, value):
    if not root:
        return None
    if root.value == value:
        return root
    left = find_node(root.left, value)
    if left:
        return left
    return find_node(root.right, value)

def user_input_lca():
    values = list(map(lambda x: int(x) if x != 'null' else None, input("Enter the tree nodes (use 'null' for None, space-separated): ").split()))
    root = build_tree_from_list(values)
    p_value = int(input("Enter value of node p: "))
    q_value = int(input("Enter value of node q: "))
    
    p = find_node(root, p_value)
    q = find_node(root, q_value)
    
    lca = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p_value} and {q_value} is: {lca.value if lca else 'None'}")

def test_cases():
    test_data = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4),
        ([1, 2], 1, 2)
    ]
    for i, (values, p_value, q_value) in enumerate(test_data):
        root = build_tree_from_list(values)
        p = find_node(root, p_value)
        q = find_node(root, q_value)
        lca = lowest_common_ancestor(root, p, q)
        print(f"Test Case {i + 1}: LCA of {p_value} and {q_value} is {lca.value if lca else 'None'}")


test_cases()
user_input_lca()
