from queue import PriorityQueue
from typing import Optional, List

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
        print("\n")
        print("GRAPH")
        for node in self.nodes:
            print("Node:", node.value)
            print("Edges:")
            for edge in node.edges:
                print(edge.node_origin.value, "<-- ", edge.weight, " -->", edge.node_destination.value)
        print("\n")

    def hill_climb(self, start_value: str, goal_value: str) -> List[str]:
        start_node = self.find_node(start_value)
        goal_node = self.find_node(goal_value)

        if not start_node or not goal_node:
            print("Start or goal node not found.")
            return []

        # Priority queue to prioritize nodes with lower heuristic values
        frontier = PriorityQueue()
        frontier.put((0, [start_node.value]))  # (heuristic value, [path])
        explored = set()  # Set to store explored nodes

        while not frontier.empty():
            current_cost, current_path = frontier.get()
            current_node = self.find_node(current_path[-1])

            if current_node.value == goal_node.value:
                return current_path  # Return the path if the goal node is reached

            if current_node.value not in explored:
                explored.add(current_node.value)
                # Calculate heuristic (in this case, we assume a simple heuristic of 1)
                heuristic = 1

                # Expand to neighboring nodes
                for edge in current_node.edges:
                    neighbor_node = edge.node_destination if edge.node_origin.value == current_node.value else edge.node_origin
                    neighbor_cost = current_cost + edge.weight
                    neighbor_path = current_path + [neighbor_node.value]
                    frontier.put((neighbor_cost + heuristic, neighbor_path))  # Add to frontier with priority

        print("Goal not reachable.")
        return []

    @staticmethod
    def print_path(path: list) -> None:
        print("\n[Hill Climbing]")
        if not path:
            print("Path is empty")
            return

        print("Path:", end=" ")
        for idx, item in enumerate(path):
            if idx == len(path) - 1:  # Last item in path
                print(item, end="")  # Print without arrow
            else:
                print(item, "->", end=" ")  # Print with arrow
        print()  # Add a new line after printing the path
