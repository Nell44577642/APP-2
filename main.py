
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
