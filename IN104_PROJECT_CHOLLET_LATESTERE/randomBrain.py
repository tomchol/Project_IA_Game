import random

class RandomBrain:
    def __init__(self):
        self.name = "OrdiRand"
        self.alwaysSeeAsWhite = False

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        n=len(possibleMoves)
        a=random.randint(0,n-1)
        return possibleMoves[a]

    def __str__(self):
        return "Random_Player"
