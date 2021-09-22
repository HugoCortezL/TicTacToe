from Map import Map
from Player import Player

class Game:
    def __init__(self, map:Map, player1:Player, player2:Player):
        self.map = map
        self.player1 = player1
        self.player2 = player2
        self.currentPlayer = player1
        self.nextPlayer = player2
        self.continueGame = True
    
    def startRound(self):
        print(self.currentPlayer.name, 'plays')
        self.map.printMap()
        position:int = int(input("Choose a position: "))
        while position < 1 or position > 9:
            position = int(input("Choose a position: "))
        self.map.move(self.currentPlayer, position)
        print()
    
    def restartMatch(self):
        self.map.restartMap()
    
    def changeCurretPlayer(self):
        anchor:Player = self.nextPlayer
        self.nextPlayer = self.currentPlayer
        self.currentPlayer = anchor

    def endMatch(self, champion:Player):
        if champion == None:
            self.changeCurretPlayer()
            return False
        else:
            self.map.printMap()
            print('\033[1;32;40m','WINNER' ,champion.name, '\033[0m')
            print()
            restart = input("Do you want to restart the game? (Y/N)")
            if(restart.upper() == 'Y'):
                self.restartMatch()
            else:
                self.continueGame = False
            return True
    
    def endRound(self):
        champion:Player = self.map.endMatch(self.currentPlayer, self.nextPlayer)
        if champion == None:
            self.changeCurretPlayer()
        else:
            self.endMatch(champion)
