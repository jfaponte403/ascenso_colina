from typing import Optional

from Entity.Edge import Edge
from Entity.Node import Node


class Graph:
    def __init__(self):
        self.nodes: list[Node] = []

    def add_node(self, value: str) -> Node:
        node = Node(value)
        self.nodes.append(node)
        return node

    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
        if node1 and node2:
            edge = Edge(node1, node2, weight)
            node1.add_edge(edge)
            node2.add_edge(edge)
        else:
            print("One or more nodes not found.")

    def find_node(self, value: str) -> Optional[Node]:
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def display(self):
        for node in self.nodes:
            print("Node:", node.value)
            print("Edges:")
            for edge in node.edges:
                print(edge.node_origin.value, "<-- ", edge.weight, " -->", edge.node_destination.value)
