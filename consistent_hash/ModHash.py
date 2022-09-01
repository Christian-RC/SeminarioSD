#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 rzavalet <rzavalet@noemail.com>
#
# Distributed under terms of the MIT license.

"""
An implementation of a Hash using mod.
Please implement the requiered methods.
"""
from bisect import bisect_left
from HashScheme import HashScheme
import hashlib


class ModHash(HashScheme):

    def __init__(self):
        """
        You have to decide what members to add to the class
        """
        self.__scheme_name = 'Modular_Hash'
        self.nodes = {}

    def __get_hash(self, value):
        return (int(hashlib.md5(value.encode()).hexdigest(), 16) % 3)

    def get_name(self):
        return self.__scheme_name

    def dump(self):
        """
        Auxiliary method to print out information about the hash
        """
        for k in self.nodes.keys():
            print("Node: {0} hash: {1}".format(self.nodes[k], k))

    def add_node(self, new_node):
        """
        Possibly just increment a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        hash_value = self.__get_hash(new_node)
        if hash_value not in self.nodes.keys():
            # --> nodos[valor_hash] = nombre_nodo
            self.nodes[hash_value] = new_node
            return 0
        return 1

    def remove_node(self, node):
        """
        Possibly just decrement a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        hash_value = self.__get_hash(node)
        if hash_value in self.nodes.keys():
            del self.nodes[hash_value]
            return 0
        return 1

    def hash(self, value):
        """
        Convert value to a number representation and then obtain mod(number_of_nodes)
        """
        if len(self.nodes.keys()) == 0:
            return None

        # --> valor en representación numérica
        hash_value = self.__get_hash(value)

        # --> lista con llaves de los nodos ordenadas
        sorted_nodes = sorted(self.nodes.keys())
        r = len(sorted_nodes) - 1
        l = 0

        if hash_value < sorted_nodes[0] or hash_value >= sorted_nodes[r]:
            return self.nodes[sorted_nodes[r]]

        found_index = bisect_left(sorted_nodes, hash_value)
        if sorted_nodes[found_index] != hash_value:
            found_index -= 1

        return self.nodes[sorted_nodes[found_index]]
