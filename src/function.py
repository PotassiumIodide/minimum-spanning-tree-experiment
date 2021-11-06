def functionize(dictionary):
	"""辞書型の引数を関数へ変換する関数

	Args:
		dictionary: 関数の対応を表した辞書

	Returns:
	    辞書を関数にしたもの
	"""
	return lambda x: dictionary[x]


def generalize(func):
	"""集合Aから実数Rへの関数f: A → Rを，べき集合P(A)からの関数へ一般化する関数

	Args:
		func: 集合Aから実数Rへの関数

	Returns:
		べき集合P(A)から実数Rへの関数
	"""
	return lambda X: sum(func(x) for x in X) if isinstance(X, set) else func(X)