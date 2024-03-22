

class TreeEdge:
    def __init__(self, node_origin, node_destination, weight: int = 1):
        self.tree_node_origin = node_origin
        self.tree_node_destination = node_destination
        self.weight = weight
