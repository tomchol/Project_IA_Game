import aiarena
import time
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_time_alphabeta_tt import minimax
from .evaluation_functions import connect4, checkers, abalone

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate,
    aiarena.abalone: abalone.evaluate
}

#definition de la fonction qui va calculer T_recherche pour l'IA
def compute_research_time (GameState,evaluate):
	init=time.time()
	A = GameState.findNextStates()
	#evaluate(A[0])
	return(time.time()-init)
	


class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.T_limit = 2
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]
        
        #On va prendre le maximum de 50 T_recherche afin de s'assurer que l'on ne dépasse jamais la limite de temps impartie 
        maxi=0
        for loop in range(50):
        	a=compute_research_time(gameclass.GameState(),self.evaluate)
        	if a>maxi:
        		maxi=a
        self.T_recherche= maxi
	
		

    def play(self, gameState, timeLimit):
    	tac = time.time()
    	
    	states=gameState.findNextStates()
    	moves = gameState.findPossibleMoves()
    	
    	#Nombre d'enfants
    	nmb = len(states)
    	
    	toc = time.time()
    	
    	#Temps à donner aux enfants
    	T_limit_enfants = (self.T_limit + tac - toc)
    	
    	tic = time.time()
    	maxi=minimax(states[0], False, self.get_children, self.evaluate, T_limit_enfants/nmb,self.T_recherche)
    	tuc = time.time()
    	
    	N = 1
    	nmaxi=0
    	n=1
    	for element in states[1:]:
    		#On met à jour T_limit en fonction du temps pris par la recherche precedente pour donner plus de temps aux recherches suivantes
    		T_limit_enfants += ((T_limit_enfants)/(nmb) - (tuc - tic))*nmb/(nmb-N)
    		tic = time.time()
    		minim =minimax(element, False, self.get_children, self.evaluate, T_limit_enfants/nmb,self.T_recherche)
    		if minim>maxi:
    			maxi=minim
    			nmaxi=n
    		n=n+1
    		N = N+1
    		tuc = time.time()
    	return moves[nmaxi]
        
	
        
            

    def __str__(self):
        return "MiniMax_Player"


