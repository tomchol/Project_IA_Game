from aiarena.abalone import cell
import math as m

def evaluate(gs): 
	if gs.capturedWhiteBalls == 3 :
		return -m.inf
	if gs.capturedBlackBalls == 3 :
		return m.inf
	score = (gs.capturedWhiteBalls - gs.capturedBlackBalls)*1000
	for i in range (9) :
		for j in range(max(i-4,0), min(9,i+5)) :
			mult  = 2* (gs.getCell(i,j).color == cell.WHITE) -1
			score += mult*score_position(i,j)
			score += mult*score_groupement(gs,i,j)
	return score
	
	

def score_position(i,j) :
	return (4-abs(4-i))*5 + (min(9,i+5)-(max(i-5,0))//2 - abs(min(9,i+5)-(max(i-5,0))//2 - j))*5
	
	
def score_groupement(gs,i,j):
	compteur_voisins = 0
	A = gs.getCell(i,j)
	if i>0 and j<i+4 and gs.getCell(i-1,j) == A:
		compteur_voisins +=1
	if i<8 and j>i-4 and gs.getCell(i+1,j) == A:
		compteur_voisins +=1
	if j>0 and i<j-4 and gs.getCell(i,j-1) == A:
		compeur_voisins += 1
	if j<8 and i>j+4 and gs.getCell(i,j+1) == A:
		compteur_voisins +=1
	if i>0 and j>0 and gs.getCell(j-1, j-1) == A:
		compeur_voisins +=1
	if j<8 and i<8 and gs.getCell(i+1, j+1) == A:
		compteur_voisins +=1
	return compteur_voisins
