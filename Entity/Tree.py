from Entity.Graph import Graph
from Entity.Node import Node


class Tree:
    def __init__(self, origin: Node, graph: Graph):
        self.root = origin
        self.graph = graph
        self.children = []

    def load_tree_from_graph_and_node(self, node=None):
        if node is None:
            node = self.root

        edges = self.graph.get_edges(node)

        for edge in edges:
            print(f"origin: {edge.origin.value} -> destination: {edge.destination.value} : {edge.weight}")
            self.load_tree_from_graph_and_node(edge.destination)

    # def load_tree_from_graph_and_node(self):
    #     next_node = None
    #     edges = self.graph.get_edges(self.root)
    #
    #     for edge in edges:
    #         print(f"origin: {edge.origin.value} -> destination: {edge.destination.value} : {edge.weight}")
    #         next_node = edge.destination
    #
    #     next_edges = self.graph.get_edges(next_node)
    #
    #     for edge in next_edges:
    #         print(f"origin: {edge.origin.value} -> destination: {edge.destination.value} : {edge.weight}")
    #         next_node = edge.destination
