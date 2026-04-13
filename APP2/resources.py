class BidNode:
    def __init__(self, price, player):
        self.price = price
        # We need a list because if 2 people bid 10, nobody wins
        self.players = [player] 
        self.left = None
        self.right = None

class AuctionBST:
    def __init__(self):
        self.root = None

    # Logic to insert without using .sort() as requested
    def insert(self, price, player):
        if not self.root:
            self.root = BidNode(price, player)
        else:
            self._add_recursive(self.root, price, player)

    def _add_recursive(self, current, price, player):
        if price == current.price:
            # Tie case: add to the list of names at this price
            current.players.append(player)
        elif price < current.price:
            if current.left is None:
                current.left = BidNode(price, player)
            else:
                self._add_recursive(current.left, price, player)
        else:
            if current.right is None:
                current.right = BidNode(price, player)
            else:
                self._add_recursive(current.right, price, player)

    # In-order traversal: Left -> Root -> Right (gives us sorted prices)
    def get_sorted_list(self):
        results = []
        self._traverse(self.root, results)
        return results

    def _traverse(self, node, results):
        if node:
            self._traverse(node.left, results)
            results.append((node.price, node.players))
            self._traverse(node.right, results)

    def find_winner(self):
        # We look for the first (lowest) price with only 1 player
        all_bids = self.get_sorted_list()
        for price, players in all_bids:
            if len(players) == 1:
                return price, players[0]
        return None, None

    # The formula from the PDF: bid_cost = base + alpha / (price + 1)
    def calculate_cost(self, price, alpha, base):
        return base + (alpha / (price + 1))