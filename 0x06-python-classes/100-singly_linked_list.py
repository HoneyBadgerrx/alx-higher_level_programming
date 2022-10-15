#!/usr/bin/python3
""" singly linked lists """
class node:
    """ represents  node in list"""
    def __init__(self, data, next_node=None):
        """initialises node"""
        self.data = data
        self.next_node = next_node
