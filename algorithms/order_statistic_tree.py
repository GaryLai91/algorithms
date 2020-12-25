from avl import AVLNode, AVL


class OSNode(AVLNode):
    """Implementation of Order Statistic Node"""
    def __init__(self, key):
        AVLNode.__init__(self, key)
        self.size = 0

    def update_subtree_info(self):
        self.height = self._uncached_height()
        self.size = self._uncached_size()

    def _uncached_size(self):
        left_size = 0
        right_size = 0
        if self.left:
            left_size = self.left.size
        if self.right:
            right_size = self.right.size
        return left_size + right_size + 1


class OSTree(AVL):
    """ Implementation of Order Statistic Tree"""
    def __init__(self, node_class=OSNode):
        super().__init__(node_class)

    def select(self, node, rank):
        """
        Given a rank (an index), returns a pointer to the node
        containing the i-th smallest key in the subtree rooted at node
        """
        # compute the rank of node given
        r = 1
        if node.left:
            r = node.left.size + 1
        if rank == r:
            return node
        elif rank < r:
            return self.select(node.left, rank)
        else:
            return self.select(node.right, rank - r)
        return node