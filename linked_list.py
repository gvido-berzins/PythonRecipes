"""
Summary:
    Simple Python implementation of a linked list
Description:
    Learned from https://realpython.com/linked-lists-python/
    check them out
"""
from dataclasses import dataclass
from typing import TypeVar

TNode = TypeVar("TNode", bound="Node")


@dataclass
class Node:
    data: str
    next: TNode = None

    def __str__(self):
        return self.data


@dataclass
class LinkedList:
    head: Node = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


def link():
    node_a = Node("Data1")
    node_b = Node("Data2")
    node_c = Node("Data3")
    node_d = Node("Data4")

    llist = LinkedList()
    llist.head = node_a
    print(llist)

    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d

    print(llist)
    for node in llist:
        print(node)


if __name__ == "__main__":
    link()
