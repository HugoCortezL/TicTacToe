from Player import Player

class Map:
    def __init__(self):
        self.map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def printMap(self):
        line:int = 0
        for square in self.map:
            print(square, end="")
            line += 1
            if line <= 2:
                print('|', end="")
            elif line == 3:
                print()
                line = 0
        print()
    
    def restartMap(self):
        self.map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def move(self, player:Player, square:int):
        self.map[square-1] = player.symbol
    
    def validPlayerWin(self, player:Player):
        if self.map[0] == player.symbol:
            if self.map[1] == player.symbol:
                if self.map[2] == player.symbol:
                    return True
            if self.map[4] == player.symbol:
                if self.map[8] == player.symbol:
                    return True
            if self.map[3] == player.symbol:
                if self.map[6] == player.symbol:
                    return True
        if self.map[1] == player.symbol:
            if self.map[4] == player.symbol:
                if self.map[7] == player.symbol:
                    return True
        if self.map[2] == player.symbol:
            if self.map[5] == player.symbol:
                if self.map[8] == player.symbol:
                    return True
            if self.map[4] == player.symbol:
                if self.map[6] == player.symbol:
                    return True
        if self.map[3] == player.symbol:
            if self.map[4] == player.symbol:
                if self.map[5] == player.symbol:
                    return True
        if self.map[6] == player.symbol:
            if self.map[7] == player.symbol:
                if self.map[8] == player.symbol:
                    return True
        return False




    def endMatch(self, player1:Player, player2:Player):
        if self.validPlayerWin(player1):
            return player1
        elif self.validPlayerWin(player2):
            return player2
        else:
            return None
