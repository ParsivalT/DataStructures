"""
    A node contains stores data and memory addressof the next node.
"""


class Node:
    """
    class responsible for defininf nodes.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
