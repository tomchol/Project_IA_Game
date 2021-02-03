# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxTimeBrain import MinimaxBrain


brain1 = MinimaxBrain(aiarena.connect4)
brain1.depth = 5
brain2 = MinimaxBrain(aiarena.connect4)
brain2.depth = 5
ai_time = 2 #the AI will only have 1 sec to play
game = aiarena.Game(aiarena.connect4, brain1, ai_time, brain2, ai_time)
game.displayLevel = 1   # this prints the board after each move
game.start()
print(game.pgn) #print the summary of the game. 

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames
