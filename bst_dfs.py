class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        answer = [[root.val]]
        while queue:
            child = []
            for node in queue:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if not child: #last level of tree.
                break
            queue = child #assigning this level to queue.
            answer.append([node.val for node in queue])
			
        return answer[::-1]