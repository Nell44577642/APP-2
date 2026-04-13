import random
from resources import AuctionBST

class AuctionController:
    def __init__(self):
        self.view = None
        self.tree = AuctionBST()
        # Constants from the APP requirements
        self.alpha = 50.0 
        self.base_fee = 2.0

    def handle_human_bid(self, name, price):
        if not name: name = "Anonymous"
        self.tree.insert(price, name)
        # Show the user the cost of their specific bid
        cost = self.tree.calculate_cost(price, self.alpha, self.base_fee)
        self.view.update_log(f"{name} bid {price}€ (Fee paid: {cost:.2f}€)")

    def add_bots(self):
        # Some variety of bot behaviors
        bots = ["Aggressive_Bot", "Safe_Bot", "Random_Bot", "Cheap_Bot"]
        for b in bots:
            # Each bot picks a random number between 0 and 20
            p = random.randint(0, 20)
            self.tree.insert(p, b)
        self.view.update_log("Added 4 AI competitors to the tree.")

    def show_results(self):
        win_p, win_n = self.tree.find_winner()
        all_data = self.tree.get_sorted_list()
        
        # Calculate revenue for the startup
        total_rev = 0
        for p, players in all_data:
            cost_per_bid = self.tree.calculate_cost(p, self.alpha, self.base_fee)
            total_rev += cost_per_bid * len(players)
            
        self.view.update_log("\n--- AUCTION FINALIZED ---")
        if win_n:
            self.view.update_log(f"WINNER: {win_n} at {win_p}€")
        else:
            self.view.update_log("RESULT: No winner found (everyone tied!)")
        
        self.view.update_log(f"STARTUP REVENUE: {total_rev:.2f}€")
        self.view.update_log("-" * 25)

    def reset(self):
        self.tree = AuctionBST()
        self.view.update_log("Auction cleared. Ready for new bids.")