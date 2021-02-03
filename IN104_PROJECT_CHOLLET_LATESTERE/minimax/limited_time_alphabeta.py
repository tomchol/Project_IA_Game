import time
import math as m
def minimax(node, maximize, get_children, evaluate,T_limit,T_recherche,alpha=-m.inf, beta=m.inf):
	tic=time.time()
	#Si plus assez de temps, on evalue le noeud actuel
	if (T_recherche > T_limit):
		return evaluate(node)
	noeudsEnfant = get_children(node)
	
	#Si il n'y a plus de coup possible après, on evalue le noeud actuel
	nmbEnfants = len(noeudsEnfant)
	if nmbEnfants == 0 :
		return evaluate(node)

	#On initialise la liste prenant les valeurs des noeuds des enfants
	minmaxEnfant = []
	tac = time.time()
	T_limit_enfants = (T_limit + tic - tac)
	n = 0 
	for element in noeudsEnfant :
		toc = time.time()
		mimaElement = minimax(element, not maximize, get_children, evaluate,(T_limit_enfants/nmbEnfants),T_recherche,alpha,beta)

		#Si on se rend compte qu'on n'a pas besoin d'explorer les autres enfants
		#On renvoie la valeur du noeud enfant qu'on regarde en ce moment directement
		if maximize and mimaElement >=beta:
			return mimaElement
		elif (not maximize) and mimaElement<=alpha:
			return mimaElement

		#On met eventuellement à jour la valeur de beta ou alpha
		if (not maximize) and mimaElement <beta:
			beta =mimaElement
		elif maximize and mimaElement > alpha:
			alpha = mimaElement
		minmaxEnfant.append(mimaElement)
		n += 1
		tuc = time.time()

		#On met à jour le temps restant en fonction du temps pris par l'exploration des noeuds précédents pour éventuellement donner plus de temps pour trouver les valeurs des noeuds suivants
		#La condition est ici pour le dernier tour de boucle
		if nmbEnfants-n != 0 :
			T_limit_enfants += ((T_limit_enfants)/(nmbEnfants) - (tuc - toc))*nmbEnfants/(nmbEnfants-n)
	
	#On retourne le max où le min des valeurs des noeuds des enfants en fonction de maximize
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


