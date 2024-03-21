from Entity.Node import Node


class Edge:
    def __init__(self, origin: Node, destination: Node, weight: int):
        self.origin = origin
        self.destination = destination
        self.weight = weight


