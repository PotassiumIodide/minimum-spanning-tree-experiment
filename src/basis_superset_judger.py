def by_independent_sets(independent_sets):
	"""独立集合族Tにより与えられた集合が基拡大集合か否か判定する関数を返す関数

	Args:
		independent_sets: 独立集合族T

	Returns:
		与えられた集合Xが基拡大集合か否か判定する関数
	    True if |X| ≧ max{|I|: I ∈ T} False otherwise
	"""
	return lambda X: len(X) >= max(len(I) for I in independent_sets)


def by_bases(bases):
	"""基族Dにより与えられた集合が基拡大集合か否か判定する関数を返す関数

	Args:
		bases: 基族D

	Returns:
		与えられた集合Xが従属か否か判定する関数
	    True if ∃B ∈ D, B ⊊ X    False otherwise
	"""
	return lambda X: any(B <= X for B in bases)


def by_rank_function(rank_function, ground_set):
	"""階数関数ρにより与えられた集合が基拡大集合か否か判定する関数を返す関数

	Args:
		rank_function: 階数関数ρ
		ground_set: 台集合E
	
	Returns:
	    与えられた集合Xが従属か否か判定する関数
		True if ρ(X) == ρ(E)     False otherwise
	"""
	return lambda X: rank_function(X) == rank_function(ground_set)