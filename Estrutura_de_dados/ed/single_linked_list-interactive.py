# coding: utf-8

__author__ = 'Kaio Oliveira'

'''
Linked list is a linear data structure that contains sequence of elements
such that each element links to its next element in the sequence.

Each element in a linked list is called as "Node".
'''

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, element):
        node = self.head

        if element is not None:
            while node.next is not None:
                if(node.data == element):
                    return node

                node = node.next

            if node.data == element:
                return node

        return None

    def insert(self, element):
        new_node = Node(element)

        if self.head == None:
            self.head = new_node
        else:
            aux = self.head

            while aux.data is not None:
                aux = aux.next

            aux = new_node

    def remove(self, element):
        if element is not None:
            if self.head.data == element:
                self.head = None
            else:
                previous = Node(None)
                aux = self.head

                while aux.data is not None and aux.data != element:
                    previous = aux
                    aux = aux.next

                if aux.data is not None:
                    previous.next = aux.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
