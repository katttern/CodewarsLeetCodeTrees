# Pre-order traversal
def pre_order(node):
    result = []
    def recursive_pre(n):
        if n is None:
            return
        
        result.append(n.data)
        recursive_pre(n.left)
        recursive_pre(n.right)
    
    recursive_pre(node)
    return result

# In-order traversal
def in_order(node):
    result = []
    def recursive_in(n):
        if n is None:
            return
        
        recursive_in(n.left)
        result.append(n.data)
        recursive_in(n.right)
    
    recursive_in(node)
    return result

# Post-order traversal
def post_order(node):
    result = []
    def recursive_post(n):
        if n is None:
            return
        
        recursive_post(n.left)
        recursive_post(n.right)
        result.append(n.data)
    
    recursive_post(node)
    return result
