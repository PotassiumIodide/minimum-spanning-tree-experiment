def by_independent_sets(independent_sets):
	"""独立集合族Tにより与えられた集合が独立か否か判定する関数を返す関数

	Args:
		independent_sets: 独立集合族T

	Returns:
		与えられた集合Xが独立か否か判定する関数
	    True if X ∈ T    False otherwise
	"""
	return lambda X: X in independent_sets


def by_bases(bases):
	"""基族Dにより与えられた集合が独立か否か判定する関数を返す関数

	Args:
		bases: 基族D

	Returns:
		与えられた集合Xが独立か否か判定する関数
	    True if ∃B ∈ D, X ⊆ B    False otherwise
	"""
	return lambda X: any(X <= B for B in bases)


def by_rank_function(rank_function):
	"""階数関数ρにより与えられた集合が独立か否か判定する関数を返す関数

	Args:
		rank_function: 階数関数ρ
	
	Returns:
	    与えられた集合Xが独立か否か判定する関数
		True if ρ(X) = |X|     False otherwise
	"""
	return lambda X: rank_function(X) == len(X)