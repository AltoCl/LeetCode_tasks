# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
#
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
#
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
#
# The level of a node is the number of edges along the path between it and the root node.


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Helper function to perform BFS and reverse odd levels
        def bfs_and_reverse(node):
            queue = [node]
            level = 0

            while queue:
                level_size = len(queue)
                current_level = []
                next_queue = []

                for i in range(level_size):
                    current_node = queue[i]
                    current_level.append(current_node)
                    if current_node.left and current_node.right:
                        next_queue.append(current_node.left)
                        next_queue.append(current_node.right)

                # Reverse node values at odd levels
                if level % 2 == 1:
                    start, end = 0, len(current_level) - 1
                    while start < end:
                        current_level[start].val, current_level[end].val = current_level[end].val, current_level[start].val
                        start += 1
                        end -= 1

                queue = next_queue
                level += 1

        bfs_and_reverse(root)
        return root