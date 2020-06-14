# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.traverse = []
        def inOrderTraversal(node):
            if node is not None:
                inOrderTraversal(node.left)
                self.traverse.append(node.val)
                inOrderTraversal(node.right)

        inOrderTraversal(root)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            return self.traverse.pop(0)
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.traverse) != 0:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()