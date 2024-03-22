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
        # Buscar el nodo de inicio y el nodo objetivo en el grafo
        start_node = self.find_node(start_value)
        goal_node = self.find_node(goal_value)

        # Comprobar si el nodo de inicio y el nodo objetivo existen en el grafo
        if not start_node or not goal_node:
            print("Start or goal node not found.")
            return []

        # Inicializar la cola de prioridad para almacenar nodos que se van a explorar
        frontier = PriorityQueue()
        # Agregar el nodo de inicio con costo 0 a la cola de prioridad, con el camino formado solo por el nodo de inicio
        frontier.put((0, [start_node.value]))
        # Inicializar un conjunto para almacenar nodos explorados
        explored = set()

        # Mientras haya nodos en la cola de prioridad
        while not frontier.empty():
            # Extraer el nodo actual y su costo asociado de la cola de prioridad
            current_cost, current_path = frontier.get()
            # Encontrar el nodo actual en el grafo
            current_node = self.find_node(current_path[-1])

            # Comprobar si el nodo actual es el nodo objetivo
            if current_node.value == goal_node.value:
                # Devolver el camino actual si se alcanza el nodo objetivo
                return current_path

                # Si el nodo actual no ha sido explorado
            if current_node.value not in explored:
                # Marcar el nodo actual como explorado
                explored.add(current_node.value)

                # Definir la heurística (en este caso, 1)
                heuristic = 1

                # Expandir a los nodos vecinos del nodo actual
                for edge in current_node.edges:
                    # Determinar el nodo vecino basado en la arista y el nodo actual
                    neighbor_node = edge.node_destination if edge.node_origin.value == current_node.value else edge.node_origin
                    # Calcular el costo hasta el nodo vecino
                    neighbor_cost = current_cost + edge.weight
                    # Formar el nuevo camino agregando el nodo vecino al camino actual
                    neighbor_path = current_path + [neighbor_node.value]
                    # Agregar el nodo vecino a la cola de prioridad con el costo estimado total
                    frontier.put((neighbor_cost + heuristic, neighbor_path))

                    # Si no se encuentra ningún camino al nodo objetivo
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
