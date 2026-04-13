# PBL-2  
MVP Status: v1.0  

Group Members: Bultez Charlotte, Ito-Russo Kana, Raux Lily & Ribeiro Nell  

---

##  Project Overview  
Our application simulates an auction system called **“Lowest Unique Bid Wins”**.  

In this system, the winner is the player who places the **lowest bid that is unique** (no other player chose the same price).  

Unlike traditional auctions, players must adopt a strategy:  
- bidding too low is risky because many players may choose the same value  
- bidding higher reduces duplication but increases the price  

Each bid has a cost, which allows the startup to generate revenue from every attempt.  
This project combines **algorithmic design (Binary Search Tree)** and **economic strategy**.

---

##  Quick Start 

Clone the repository:

git clone [your-repo-link]
cd [project-folder]

Setup Virtual Environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run Application:
python main.py


⚠️ No additional installation is required (Tkinter is included with Python).

---

##  Technical Architecture  

The project follows an **MVC (Model - View - Controller)** structure.

### 🔹 main.py  
Entry point of the program.  
It initializes the controller and the interface, then launches the application.

---

### 🔹 controller/  
Handles the **application logic** and interactions.

Main features:
- `handle_human_bid()` → adds a player bid  
- `add_bots()` → adds AI players  
- `show_results()` → calculates winner and revenue  
- `reset()` → clears the auction  

---

### 🔹 resources/ (Model)  
Contains the **Binary Search Tree (BST)** used to store bids.

Key features:
- Stores bids without using Python `.sort()`  
- Allows multiple players for the same price  
- Maintains sorted order automatically  

Main methods:
- `insert(price, player)` → adds a bid  
- `get_sorted_list()` → returns sorted bids (in-order traversal)  
- `find_winner()` → finds the lowest unique bid  
- `calculate_cost()` → computes the cost of a bid  

---

### 🔹 view/  
Graphical interface built with **Tkinter**.

Features:
- Input fields (name and bid)  
- Buttons (add bots, calculate winner, reset)  
- Log display showing auction activity  

---

##  Cost Formula  

Each bid has a cost defined by:

\[
\text{cost} = base + \frac{\alpha}{price+1}
\]

In our implementation:
- `base = 2`  
- `alpha = 50`  

### Interpretation:
- Very low bids (0, 1, 2) are **expensive**  
- Higher bids are **cheaper**  
- This prevents players from always choosing the lowest values  

---

##  Winner Rule  

The winner is:
> the player who placed the **lowest unique bid**

Example:
- Bids: 1, 1, 2, 3  
- Winner → 2  

If all bids are duplicated:
> ❌ No winner  

---

##  AI Players  

The system includes several bot strategies:
- **Aggressive Bot** → bids high values  
- **Safe Bot** → bids moderate values  
- **Random Bot** → unpredictable  
- **Cheap Bot** → very low bids  

These bots simulate different player behaviors and make the game more dynamic.

---

##  Revenue Model  

The startup earns money from **every bid placed**, not only the winning one.

Total revenue is:
> the sum of all bid costs  

This creates a **game effect**:
- more players → more bids → more revenue  

---

##  Why a Binary Search Tree?  

The BST is used to:
- Keep bids **sorted automatically**  
- Avoid using Python sorting (project requirement)  
- Efficiently find the lowest unique bid  

⚠️ Limitation:
- The BST can become inefficient if it becomes **unbalanced**  

---

##  Testing & Validation  

To test the program:

- Place several bids  
- Add bots  
- Click “Calculate Winner”  

Check that:
- bids are correctly stored  
- prices are sorted  
- the correct winner is displayed  
- total revenue is correct  

### ✅ Happy Path:
- At least one unique bid exists  
- The system correctly returns:
  - the winner  
  - the winning price  
  - total revenue  

---

##  Future Improvements (v2.0)

- Improve bot behavior (fix logic and add strategies)  
- Add multi-round simulations  
- Implement a balanced BST  
- Add statistics (win rate, average cost, revenue analysis)  
- Improve user interface  

---

##  How to Use  

1. Enter your name and a bid  
2. Click **“Bid!”**  
3. Add bots  
4. Click **“Calculate Winner”**  
5. View results in the log  

---
