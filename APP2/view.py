import tkinter as tk
from tkinter import messagebox

class AuctionView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("LowBid")
        self.window.geometry("550x600")
        
        # Header
        tk.Label(self.window, text="Lowest Unique Bid Wins !", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Human Interaction Area
        input_frame = tk.LabelFrame(self.window, text=" Place your bid here ", padx=10, pady=10)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(input_frame, text="Your Name:").grid(row=0, column=0)
        self.name_in = tk.Entry(input_frame)
        self.name_in.grid(row=0, column=1, padx=5)
        
        tk.Label(input_frame, text="Bid (€):").grid(row=0, column=2)
        self.bid_in = tk.Entry(input_frame)
        self.bid_in.grid(row=0, column=3, padx=5)
        
        tk.Button(input_frame, text="Bid!", command=self.on_bid_click, bg="lightblue").grid(row=0, column=4, padx=5)

        # Control Buttons
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Add AI Bots", command=self.controller.add_bots, width=15).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Calculate Winner", command=self.controller.show_results, width=15, bg="lightgreen").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Reset Board", command=self.controller.reset, width=15).grid(row=0, column=2, padx=5)

        # Log Area
        self.log = tk.Text(self.window, height=15, width=60, font=("Consolas", 9))
        self.log.pack(pady=10, padx=10)
        self.log.insert("1.0", "Welcome! Enter a bid and add bots to compete.\n" + "-"*30 + "\n")

    def on_bid_click(self):
        name = self.name_in.get()
        try:
            val = int(self.bid_in.get())
            self.controller.handle_human_bid(name, val)
            self.bid_in.delete(0, tk.END) # clear input
        except ValueError:
            messagebox.showwarning("Input Error", "The bid must be a whole number!")

    def update_log(self, text):
        self.log.config(state="normal")
        self.log.insert(tk.END, f"> {text}\n")
        self.log.see(tk.END) # Auto-scroll
        self.log.config(state="disabled")

    def run(self):
        self.window.mainloop()