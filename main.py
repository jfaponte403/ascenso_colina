from Entity.Graph import Graph
from Entity.Node import Node
from Entity.Tree import Tree

if __name__ == '__main__':
    graph_main = Graph()

    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")

    graph_main.add_edge(node_a, node_b, 5)
    graph_main.add_edge(node_a, node_c, 3)
    graph_main.add_edge(node_c, node_d, 2)
    graph_main.add_edge(node_b, node_d, 1)
    graph_main.add_edge(node_d, node_e, 2)

    graph_main.print_graph()

    print("\n")
    tree = Tree(origin=node_a, graph=graph_main)
    tree.load_tree_from_graph_and_node()
