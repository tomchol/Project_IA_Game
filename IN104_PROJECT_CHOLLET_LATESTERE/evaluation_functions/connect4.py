from aiarena.connect4 import cell
import math as m

def evaluate(gs):
	#On va regarder sur le plateau qui a l'avantage sur les suites de pions de 1,2,3 et 4+ pions
	pionsAlignes = [0,0,0,0] 
	nmbpions = 0
	for j in range(7) :
		for i in range(6):
			#A chaque fois qu'on trouve un pion, on regarde s'il est aligné avec d'autres pions dans les 4 directions possibles (ligne, colonne, 2 diagonales)
			couleur_ij = gs.getCell(i,j).color
			if (couleur_ij != cell.NONE) :
			
				#vaut 1 si pion noir, -1 si blanc
				plus_ou_moins = 2* (couleur_ij == cell.WHITE) -1
				nmbpions += 1
				
				#Val correspond à la plus longue suite de pions trouvé à partir du pion en (i,j) dans une direction
				Val = checkHoriz(gs,i,j,couleur_ij) 
				pionsAlignes[Val-1] += plus_ou_moins
				Val = checkVert(gs,i,j,couleur_ij)
				pionsAlignes[Val-1] += plus_ou_moins
				Val = checkD1(gs,i,j,couleur_ij)
				pionsAlignes[Val-1] += plus_ou_moins
				Val = checkD2(gs,i,j,couleur_ij)
				pionsAlignes[Val-1] += plus_ou_moins
				
	#si il y a un puissance 4 possible, on va lui donner plein de points, mais ce en fonction du nombre de coups qu'il faut jouer pour y arriver (privilegier les puissances 4/contres immédiats)
	if pionsAlignes[3] != 0:
		return pionsAlignes[3]/abs(pionsAlignes[3]) * 10000000 / (nmbpions)
		
	#sinon on donne des points en fonction du nombre de pions alignés
	else :
		return pionsAlignes[0] * 1 + pionsAlignes[1] * 5 + pionsAlignes[2] * 10





def checkHoriz(gs,i,j,couleur_ij):
	a, b = i, j
	compteur = 1
	#On regarde jusqu'où on peut aller vers la gauche en trouvant des pions de la même couleur
	while b>0 and gs.getCell(a,b-1).color == couleur_ij:
		b -=1
		compteur +=1
	b = j
	#Puis de même vers la droite
	while b<6 and gs.getCell(a,b+1).color == couleur_ij:
		b+=1
		compteur +=1
	if compteur >= 4:
		return 4	
	return compteur

def checkVert(gs,i,j,couleur_ij):
	a, b = i, j
	compteur = 1
	while a>0 and gs.getCell(a-1,b).color == couleur_ij:
		a -=1
		compteur +=1
	a = i
	while a<5 and gs.getCell(a+1,b).color == couleur_ij:
		a+=1
		compteur +=1
	if compteur >= 4:
		return 4
	return compteur

def checkD1(gs,i,j,couleur_ij):
	a, b = i, j
	compteur = 1	
	while a>0 and b>0 and gs.getCell(a-1,b-1).color == couleur_ij:
		a -=1
		b -=1
		compteur +=1
	a,b = i,j
	while a<5 and b<6 and gs.getCell(a+1,b+1).color == couleur_ij:
		a+=1
		b+=1
		compteur +=1
	if compteur >= 4:
		return 4	
	return compteur


def checkD2(gs,i,j,couleur_ij):
	a, b = i, j
	compteur = 1
	while a<5 and b>0 and gs.getCell(a+1,b-1).color == couleur_ij:
		a +=1
		b -=1
		compteur +=1
	a,b = i,j
	while a>0 and b<6 and gs.getCell(a-1,b+1).color == couleur_ij:
		a-=1
		b+=1
		compteur +=1
	if compteur >= 4:
		return 4
	return compteur





















