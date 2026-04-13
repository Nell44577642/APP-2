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
         # Aggressive_Bot: bids high prices to win
            if b == "Aggressive_Bot":
                p = random.randint(15, 25)
                self.tree.insert(p, "Aggressive_Bot")
        
        # Safe_Bot: bids conservatively, lower prices
            elif b == "Safe_Bot":
                p = random.randint(2, 8)
                self.tree.insert(p, "Safe_Bot")
        
        # Random_Bot: completely unpredictable
            elif b == "Random_Bot":
                p= random.randint(0, 30)
                self.tree.insert(p, "Random_Bot")
        
        # Cheap_Bot: always tries the lowest price possible
            elif b == "Cheap_Bot":
                p = random.randint(0, 3)
                self.tree.insert(p, "Cheap_Bot")

            else:
                return None

        
            
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
