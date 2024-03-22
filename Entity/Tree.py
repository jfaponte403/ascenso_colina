from queue import Queue

from Entity.TreeEdge import TreeEdge
from Entity.TreeNode import TreeNode
from Entity.Graph import Graph
from Entity.Node import Node


class Tree:
    def __init__(self, node_root: Node, graph: Graph):
        self.node_root: Node = node_root
        self.graph: Graph = graph
        self.tree_root: TreeNode = TreeNode.create_tree_node_from_graph_node(node_root)

    @staticmethod
    def add_edge(origin: TreeNode, destination: TreeNode, weight: int):
        edge = TreeEdge(origin, destination, weight)
        origin.add_child(edge)

    def load_tree(self):
        visited = set()
        q = Queue()
        q.put((self.node_root, self.tree_root))

        while not q.empty():
            current_node, parent_tree_node = q.get()
            visited.add(current_node.value)
            graph_node = self.graph.find_node(current_node.value)
            for neighbor_edge in graph_node.edges:
                neighbor_node = neighbor_edge.node_destination
                if neighbor_node.value not in visited:
                    child_tree_node = TreeNode.create_tree_node_from_graph_node(neighbor_node)
                    self.add_edge(parent_tree_node, child_tree_node, neighbor_edge.weight)

                    q.put((neighbor_node, child_tree_node))

    def display_tree(self, node: TreeNode, level=0):
        print("  " * level + node.value)
        for child_edge in node.children:
            print("  " * (level + 1) + "Peso:", child_edge.weight)
            self.display_tree(child_edge.tree_node_destination, level + 1)

    def display(self):
        if self.tree_root is not None:
            print("Árbol n-ario:")
            self.display_tree(self.tree_root)
        else:
            print("El árbol está vacío.")

    def display_ascii_tree(self, node: TreeNode, prefix="", is_tail=True):
        print(prefix + ("└── " if is_tail else "├── ") + node.value)
        children = node.children
        for i, child_edge in enumerate(children[:-1]):
            self.display_ascii_tree(child_edge.tree_node_destination, prefix + ("    " if is_tail else "│   "),
                                    is_tail=False)
        if children:
            self.display_ascii_tree(children[-1].tree_node_destination, prefix + ("    " if is_tail else "│   "),
                                    is_tail=True)

    def display_2(self):
        if self.tree_root is not None:
            print("Árbol n-ario:")
            self.display_ascii_tree(self.tree_root)
        else:
            print("El árbol está vacío.")
