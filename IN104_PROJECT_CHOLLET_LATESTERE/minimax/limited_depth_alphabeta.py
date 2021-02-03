import math as m
def minimax(node, maximize, get_children, evaluate, max_depth,alpha=-m.inf, beta=m.inf):

	#si profondeur maximale atteinte, on evalue le noeud actuel
	if (max_depth == 0):
		return evaluate(node)
	noeudsEnfant = get_children(node)

	#Si il n'y a plus de coup possible après, on evalue le noeud actuel
	if len(noeudsEnfant) == 0 :
		return evaluate(node)

	minmaxEnfant = []

	for element in noeudsEnfant :
		mimaElement = minimax(element, not maximize, get_children, evaluate,max_depth-1,alpha,beta)

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

	#On retourne le max où le min des valeurs des noeuds des enfants en fonction de maximize
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


