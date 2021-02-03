import time

def minimax(node, maximize, get_children, evaluate, T_limit,T_recherche):
	tic=time.time()
	#Si plus assez de temps, on evalue le noeud actuel
	if (T_recherche>T_limit):
		return evaluate(node)
	noeudsEnfant = get_children(node)

	#Si il n'y a plus de coup possibles après, on evalue le noeud actuel
	nmbEnfants = len(noeudsEnfant)	
	if lnmbEnfants == 0 :
		return evaluate(node)
	
	#On initialise la liste prenant les valeurs des noeuds des enfants
	minmaxEnfant = [] 
	
	tac = time.time()
	T_limit_enfants = (T_limit + tic - tac)
	n = 0

	for element in noeudsEnfant :
		toc = time.time()

		minmaxEnfant.append(minimax(element, not maximize, get_children, evaluate,(T_limit_enfants/nmbEnfants),T_recherche))
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
		
