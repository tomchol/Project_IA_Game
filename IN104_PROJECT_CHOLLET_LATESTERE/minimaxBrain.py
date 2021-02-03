import aiarena
import time
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_depth_alphabeta_tt import minimax
from .evaluation_functions import connect4, checkers

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.depth = 5     # Set the exploration depth here
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        states=gameState.findNextStates()
        moves = gameState.findPossibleMoves()
        tic = time.time()
        maxi=minimax(states[0], False, self.get_children, self.evaluate, self.depth)
        print(time.time() - tic)
        nmaxi=0
        n=0
        for element in states[1:]:
        	n=n+1
        	maxiElement = minimax(element, False, self.get_children, self.evaluate, self.depth)
        	if maxiElement >=maxi:
        		maxi=maxiElement
        		nmaxi=n
        	
        return moves[nmaxi]

	

    def __str__(self):
        return "MiniMax_Player"


