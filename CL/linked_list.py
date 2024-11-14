from __future__ import annotations  # ignore for now!


class Node:

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None) -> None:
        self.value = val
        self.next = next


two: Node = Node(2, None)
one: Node = Node(1, two)
