# PBL-2
MVP Status: [e.g., v1.0-Production]

Group Members: Bultez Charlotte, Ito-Russo Kana, Raux Lily & Ribeiro Nell

## 🎯 Project Overview
Our application simulates an auction system called “Lowest Unique Bid Wins”, where the winner is the player who places the lowest unique bid. The system also includes a cost for each bid, which allows the seller to generate revenue from every attempt. This project was built to study strategic behavior and implement an efficient way to store and process bids using a Binary Search Tree.

## 🚀 Quick Start (Architect Level: < 60s Setup)
Instructions on how to get this project running on a fresh machine.

Clone the repo:
git clone [your-repo-link]
cd [project-folder]

Setup Virtual Environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run Application:
python main.py

##🛠️ Technical Architecture
main.py: Starts the program, creates the auction, and runs the simulation.
logic/: Contains the main logic of the project:

A Binary Search Tree (BST) to store bids
Insertion of bids (with multiple players per price)
In-order traversal to get sorted prices
Function to find the lowest unique bid (winner)
Cost calculation using the formula with base_cost and alpha
ui/: Uses tkinter to allow users to interact with the system (place bids, see results).
utils/: Contains helper functions and constants (for example base_cost and alpha).
## 🧪 Testing & Validation
To verify that the program works correctly:

Run the application and place several bids
Check that bids are stored correctly in the tree
Verify that prices are sorted (in-order traversal)
Ensure that the winner is the lowest unique bid
Confirm that each bid increases the total revenue

Happy Path: 

Several players place bids
At least one price is unique
The system correctly returns the winner and total revenue

## 📦 Dependencies
tkinter: used to create the graphical interface
random: used to simulate player behavior and generate test bids


🔮 Future Roadmap (v2.0)
A CHANGER CETTE PARTIE 
Add more advanced player strategies
Improve the interface with better visualization
Implement a balanced BST to improve performance
Add multiplayer mode
Add statistics (win rate, average cost, revenue analysis)
__
