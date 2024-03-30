from node import Node


class LinkedList:
    """
    Class responsible for managing nodes.
    """

    # TODO: otimization a class adding tail
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    # TODO: create a remove function.

    # TODO: create a index function.

    # TODO: create a set function.

    # TODO: create a get function.

    def append(self, value) -> None:
        pointer = self.head

        if pointer is None:
            self.head = Node(value)

        else:
            while pointer.next:
                pointer = pointer.next

            pointer.next = Node(value)

        self._size += 1

    def __repr__(self) -> str:
        r = ""

        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next

        return r

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return self._size
