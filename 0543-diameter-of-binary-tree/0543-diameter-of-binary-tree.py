class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
            
        max_dist = 0
        depth_map = {None: 0}
        stack = [(root, False)]
        
        while stack:
            node, processed = stack.pop()
            
            if not node:
                continue
                
            if processed:
                left_depth = depth_map[node.left]
                right_depth = depth_map[node.right]
                
                max_dist = max(max_dist, left_depth + right_depth)
                depth_map[node] = 1 + max(left_depth, right_depth)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                
        return max_dist