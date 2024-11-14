"""Completing EX08!"""

from __future__ import annotations  # ignore for now!

__author__ = "730740543"


class Node:
    """Making the Node!"""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None) -> None:
        """Initialzing the object."""
        self.value = val
        self.next = next


def value_at(head: Node | None, index: int) -> int:
    """Function that finds the value at an index."""
    if head is None:  # if we have reached the end
        raise IndexError("index is out of bounds on the list.")  # ERROR !#!#
    elif index == 0:  # when we don't need to go through any more
        return head.value  # return the current value
    else:
        return value_at(head.next, index - 1)  # call yourself!


def max(head: Node | None) -> int:
    """Finds the maximum value."""
    # seperate item to refer to the next object for ease
    if head is None:  # if we got none
        raise ValueError("Cannot call max with None")  # error
    elif head.next is None:  # if we only received one item
        return head.value  # just return our singular value
    elif head.next.next is None:  # our real base case
        next_item = head.next
        # this is when we are comparing our last two items so this is the FINAL showdown
        if head.value > next_item.value:  # so if current val is greater
            return head.value
        else:
            return next_item.value
    else:  # if there is indeed more items with values
        next_item = head.next
        if head.value > next_item.value:  # if our current value
            # is greater than the next one
            # we want to 'preserve' it for future comparison
            next_item.value = head.value  # change our local object
            # so it gets the value of the current one
            # this way we dont compromise the actual linked list (or so i think)
            return max(next_item)
        else:  # otherwise if next is bigger
            return max(next_item)


def linkify(items: list[int]) -> Node | None:
    """Turns lists into linked lists."""
    if items == []:  # base case when nothing in list
        return None  # nothing more to add
    else:
        return Node(
            items[0], linkify(items[1:])
        )  # otherwise make a node with current value
        # and the next is linkifiying the rest of the items


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale every item by factor."""
    if head is None:  # base case
        return None
    else:  # if not
        return Node((head.value * factor), scale(head.next, factor))  # return a node
        # where the next value is scale(next node)
