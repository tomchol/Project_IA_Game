from aiarena.connect4 import cell
import math as m

def evaluate(gs):
	score = 0
	nmbPionts = 0
	for j in range(7) :
		for i in range(6):
			couleur_ij = gs.getCell(i,j).color
			if (couleur_ij != cell.NONE) :
				mult = 2* (couleur_ij == cell.WHITE) -1	
				nmbPionts += 1
				score += mult*checkHoriz(gs,i,j,couleur_ij)
				score += mult*checkVert(gs,i,j,couleur_ij)
				score += mult*checkD1(gs,i,j,couleur_ij)
				score += mult*checkD2(gs,i,j,couleur_ij)

	if abs(score) > 10**9 :
		return score/abs(score)*10**30/(nmbPionts**2)
	return score





def checkHoriz(gs,i,j,couleur_ij):
	a, b = i, j
	score = 0
	compteur = 1
	while b>0 and gs.getCell(a,b-1).color == couleur_ij:
		b -=1
		compteur +=1
	while b<6 and gs.getCell(a,b+1).color == couleur_ij:
		b+=1
		compteur +=1
	if compteur >= 4:
		return 10**10
	if b<6 and gs.getCell(a,b+1).color == cell.NONE:
		score +=10 * (compteur**2)
	if b>compteur-1 and gs.getCell(a,b-compteur).color == cell.NONE:
		score +=10*(compteur**2) 	
	return score



def checkVert(gs,i,j,couleur_ij):
	a, b = i, j
	score = 0
	compteur = 1	
	while a>0 and gs.getCell(a-1,b).color == couleur_ij:
		a -=1
		compteur +=1
	while a<5 and gs.getCell(a+1,b).color == couleur_ij:
		a+=1
		compteur +=1
	if compteur >= 4:
		return 10**10
	if a<5 and gs.getCell(a+1,b).color == cell.NONE:
		score +=10 * (compteur**2)
	if a>compteur-1 and gs.getCell(a-compteur,b).color == cell.NONE:
		score +=10*(compteur**2) 	
	return score


def checkD1(gs,i,j,couleur_ij):
	a, b = i, j
	compteur = 1	
	score = 0
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
		return 10**10
	if a<5 and b<6 and gs.getCell(a+1,b+1).color == cell.NONE:
		score +=10 * (compteur**2)
	if a>compteur-1 and b>compteur-1 and gs.getCell(a-compteur,b-compteur).color == cell.NONE:
		score +=10*(compteur**2) 	
	return score

def checkD2(gs,i,j,couleur_ij):
	a, b = i, j
	compteur = 1
	score = 0
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
		return 10**10
	if a<5 and b>compteur-1 and gs.getCell(a+1,b-compteur).color == cell.NONE:
		score +=10 * (compteur**2)
	if a>compteur-1 and b<6 and gs.getCell(a-compteur,b+1).color == cell.NONE:
		score +=10*(compteur**2) 	
	return score






