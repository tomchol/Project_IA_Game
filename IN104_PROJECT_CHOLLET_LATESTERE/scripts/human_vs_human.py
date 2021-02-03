# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_human
import aiarena
brain1 = aiarena.ManualBrain()
brain2 = aiarena.ManualBrain()
timeLimit = 10 # each player will have 10 seconds to play
game = aiarena.Game(aiarena.checkers, brain1, timeLimit, brain2, timeLimit)
game.start()
print(game.pgn) # display the game summary

# TODO: Placer ici le code pour lancer une partie sur n'importe quel type de jeu entre deux humains 
# à l'aide de aiarena.Game, aiarena.chess (par exemple) et aiarena.ManualBrain
#Ceci est un commentaire

