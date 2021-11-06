from src.utils.set_operator import powset

def of_independent_sets(ground_set, independent_sets):
	"""台集合と独立集合族から補独立集合族を求める関数

	Args:
		ground_set: 台集合
		independent_sets: 独立集合族

	Returns:
	    補独立集合族
	"""
	E = ground_set
	T = independent_sets
	D = [B for B in T if all(map(lambda I: not B < I, T))]
	return [X for X in powset(E) if any(not(X & B) for B in D)]


def of_bases(ground_set, bases):
	"""台集合と基族から補基族を求める関数

	Args:
		ground_set: 台集合
		bases: 基族
	
	Returns:
	    補基族
	"""
	E = ground_set
	D = bases
	return [E - B for B in D]