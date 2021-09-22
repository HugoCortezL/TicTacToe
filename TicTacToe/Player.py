class Player:
    def __init__(self, name:str, symbol:str):
        self.name = name
        self.symbol = symbol
    
    def changePlayer(self, name:str, symbol:str):
        self.name = name
        self.symbol = symbol