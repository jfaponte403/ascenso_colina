from __future__ import annotations
from typing import List

from Entity.Node import Node
from Entity.TreeEdge import TreeEdge


class TreeNode:
    def __init__(self, value: str):
        self.value: str = value
        self.children: List[TreeEdge] = []

    def add_child(self, child: TreeEdge):
        self.children.append(child)

    @staticmethod
    def create_tree_node_from_graph_node(node: Node) -> TreeNode:
        return TreeNode(node.value)
