from Map import Map
from Player import Player
from Game import Game

map = Map()

player1Name:str = None

while player1Name == None or player1Name.strip() == '':
    player1Name = input('What is the name of player 1? (X)')

player1 = Player(player1Name, 'X')

print()

player2Name:str = None

while player2Name == None or player2Name.strip() == '':
    player2Name = input('What is the name of player 2? (O)')

player2 = Player(player2Name, 'O')

game = Game(map, player1, player2)

restartMatch = True
while(game.continueGame):
    while(map.endMatch(player1, player2) == None):
        game.startRound()
        game.endRound()
