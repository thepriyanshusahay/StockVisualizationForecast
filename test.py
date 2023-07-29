class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructTree(treeStr):
    tokens = treeStr.strip().split()
    if not tokens:
        return None
    root = Node(int(tokens[0]))
    queue = [root]
    i = 1
    while queue and i < len(tokens):
        node = queue.pop(0)
        if tokens[i] != '-':
            node.left = Node(int(tokens[i]))
            queue.append(node.left)
        i += 1
        if i < len(tokens) and tokens[i] != '-':
            node.right = Node(int(tokens[i]))
            queue.append(node.right)
        i += 1
    return root

def diameterOfBT(treeStr):
    root = constructTree(treeStr)
    max_diameter = [0]
    def dfs(node):
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)
        return 1 + max(left_depth, right_depth)
    dfs(root)
    return int(str(max_diameter[0] + 1))-1
               



print(diameterOfBT('1 2 3 4 5 - 6'))