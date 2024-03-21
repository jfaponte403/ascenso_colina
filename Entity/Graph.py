from Entity.Edge import Edge
from Entity.Node import Node


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, origin: Node, destination: Node, weight: int) -> None:
        if origin not in self.graph:
            self.graph[origin] = []
        self.graph[origin].append(Edge(origin, destination, weight))

    def print_graph(self) -> None:
        for node in self.graph:
            edges = self.graph[node]
            for edge in edges:
                print(f"{edge.origin.value} -> {edge.destination.value} : {edge.weight}")

    def get_edges(self, origin: Node) -> list[Edge]:
        if origin in self.graph:
            return self.graph[origin]
        else:
            return []
