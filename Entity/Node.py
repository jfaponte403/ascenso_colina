class Node:
    def __init__(self, value: str):
        self.value: str = value
        self.edges: list = []

    def add_edge(self, edge):
        self.edges.append(edge)
