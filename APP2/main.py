# main.py
from view import AuctionView
from controller import AuctionController

def start():
    # Instantiate classes
    ctrl = AuctionController()
    ui = AuctionView(ctrl)
    
    # Connect them (MVC style)
    ctrl.view = ui
    
    # Fire it up
    ui.run()

if __name__ == "__main__":
    start()