
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

class AuctionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lowest Unique Bid Auction")

        self.auction = Auction()

        main = ttk.Frame(root)
        main.pack(padx=10, pady=10)

        self.frame_input = ttk.LabelFrame(main, text="Place Bid")
        self.frame_input.grid(row=0, column=0, padx=10)

        self.frame_display = ttk.LabelFrame(main, text="Auction State")
        self.frame_display.grid(row=0, column=1)

        self.frame_controls = ttk.LabelFrame(main, text="Controls")
        self.frame_controls.grid(row=1, column=0, columnspan=2, pady=10)

        self.build_input()
        self.build_display()
        self.build_controls()

    def build_input(self):
        ttk.Label(self.frame_input, text="Player").grid(row=0, column=0)

        self.player_entry = ttk.Entry(self.frame_input)
        self.player_entry.grid(row=0, column=1)

        ttk.Label(self.frame_input, text="Price").grid(row=1, column=0)

        self.price_entry = ttk.Entry(self.frame_input)
        self.price_entry.grid(row=1, column=1)

        ttk.Button(
            self.frame_input,
            text="Place Bid",
            command=self.place_bid
        ).grid(row=2, column=0, columnspan=2, pady=5)

    def build_display(self):
        self.text = tk.Text(self.frame_display, width=40, height=15)
        self.text.pack()

    def build_controls(self):
        ttk.Button(
            self.frame_controls,
            text="Find Winner",
            command=self.show_winner
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            self.frame_controls,
            text="Simulate 20 Bids",
            command=self.simulate
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            self.frame_controls,
            text="Show Revenue",
            command=self.show_revenue
        ).grid(row=0, column=2, padx=5)

    def place_bid(self):
        player = self.player_entry.get()
        try:
            price = int(self.price_entry.get())
        except:
            return
        self.auction.place_bid(player, price)
        self.update_display()

    def update_display(self):
        self.text.delete(1.0, tk.END)
        bids = self.auction.tree.inorder()
        for price, players in bids:
            self.text.insert(tk.END, f"{price} -> {players}\n")

    def show_winner(self):
        price, player = self.auction.winner()
        if player:
            msg = f"\nWinner: {player} with bid {price}\n"
        else:
            msg = "\nNo unique bid winner\n"
        self.text.insert(tk.END, msg)

    def show_revenue(self):
        self.text.insert(
            tk.END,
            f"\nSeller revenue: {self.auction.revenue:.2f}\n"
        )

    def simulate(self):
        players = ["Alice","Bob","Tom","Emma","Leo"]
        for _ in range(20):
            p = random.choice(players)
            price = random.randint(0,20)
            self.auction.place_bid(p, price)
        self.update_display()

root = tk.Tk()
app = AuctionGUI(root)
root.mainloop()
