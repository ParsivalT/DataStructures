from node import Node


class LinkedList:
    """
    Class responsible for managing nodes.
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    # TODO: create a remove function.

    # TODO: create a index function.

    # TODO: create a set function.

    # TODO: create a get function.

    def append(self, value) -> None:
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

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



class LinkedListNoOptimized:
    """
    Class responsible for managing nodes.
    """

    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def append(self, value) -> None:
        pointer = self.head
        if pointer is None:
            self.head = Node(value)

        else: 
            while pointer.next:
                pointer = pointer.next

            pointer.next = Node(value)



import time
def calculate_execution_time(list, param):
    init = time.time()
    for _ in range(param):
        list.append(_)

    finish = time.time()
    del list

    return finish - init


if __name__ == "__main__":
    samples =  10000

    list1= LinkedList()
    time_list1 = calculate_execution_time(list1, samples)

    print(f"the execution time of the first list was: {time_list1:.6f} seconds")

    list2 = LinkedListNoOptimized()
    time_list2 = calculate_execution_time(list2, samples)


    print(f"the execution time of the second list was: {time_list2:.6f} seconds")

