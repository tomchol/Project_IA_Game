def minimax(node, maximize, get_children, evaluate, max_depth):
	#Si profondeur maximale atteinte, on evalue le noeud actuel
	if (max_depth == 0):
		return evaluate(node)

	#Si le noeud actuel est le dernier coup possible, on evalue sa valeur
	noeudsEnfant = get_children(node)
	if len(noeudsEnfant) == 0 :
		return evaluate(node)

	minmaxEnfant = []
	for element in noeudsEnfant :
		minmaxEnfant.append(minimax(element, not maximize, get_children, evaluate,max_depth-1))

	#On retourne le max où le min des valeurs des noeuds des enfants en fonction de maximize
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


