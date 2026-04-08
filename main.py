
import tkinter as tk
from tkinter import ttk
import random

# BST NODE

class Node:
    def __init__(self, price):
        self.price = price
        self.players = []
        self.left = None
        self.right = None

# binary search tree 

class BST:

    def __init__(self):
        self.root = None

    def insert(self, price, player):
        self.root = self._insert(self.root, price, player)

    def _insert(self, node, price, player):

        if node is None:
            node = Node(price)
            node.players.append(player)
            return node

        if price < node.price:
            node.left = self._insert(node.left, price, player)

        elif price > node.price:
            node.right = self._insert(node.right, price, player)

        else:
            node.players.append(player)

        return node


    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result


    def _inorder(self, node, result):

        if node is None:
            return

        self._inorder(node.left, result)
        result.append((node.price, node.players))
        self._inorder(node.right, result)


    def lowest_unique(self):

        result = self.inorder()

        for price, players in result:
            if len(players) == 1:
                return price, players[0]

        return None, None

class Auction:

    def __init__(self, base_cost=1, alpha=10):

        self.tree = BST()
        self.base_cost = base_cost
        self.alpha = alpha
        self.revenue = 0
        self.total_bids = 0


    def bid_cost(self, price):

        return self.base_cost + self.alpha/(price+1)


    def place_bid(self, player, price):

        self.tree.insert(price, player)

        cost = self.bid_cost(price)

        self.revenue += cost
        self.total_bids += 1


  def winner(self):

        return self.tree.  lowest_unique()


