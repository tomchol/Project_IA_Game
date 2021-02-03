import math as m
def minimax(node, maximize, get_children, evaluate, max_depth,alpha=-m.inf, beta=m.inf, dico = {}):

	noeudsEnfant = get_children(node)
	#si profondeur maximale atteinte, on evalue le noeud actuel
	#Si il n'y a plus de coup possible après, on evalue le noeud actuel
	if (max_depth == 0 or len(noeudsEnfant) == 0):
		strnode=str(node)
		if strnode in dico.keys():
			return dico[strnode]
		else:
			dico[strnode]=evaluate(node)
			return dico[strnode]

	minmaxEnfant = []

	for element in noeudsEnfant :
		mimaElement = minimax(element, not maximize, get_children, evaluate,max_depth-1,alpha,beta, dico)

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
		


