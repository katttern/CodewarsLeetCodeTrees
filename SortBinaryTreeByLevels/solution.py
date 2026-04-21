def tree_by_levels(node):
    if node is None:
        return []
    result = [node.value]
    current = [node]
    while current:
        next_level = []
        for n in current:
            if n.left is not None:
                next_level.append(n.left)
            if n.right is not None:
                next_level.append(n.right)
        
        result.extend([n.value for n in next_level])
        current = next_level
        
    return result
