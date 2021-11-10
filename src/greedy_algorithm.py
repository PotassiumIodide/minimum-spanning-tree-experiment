def best_in(E, w, independence_oracle, maximize=False):
	"""最良選択貪欲法
	計算量は、n:=|E|とし、独立性オラクルの計算量をf(n)としたとき
	O(nlog(n) + nf(n))

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    independence_oracle: 独立であるかどうかを判定する関数
		maximize: Trueなら最大化、Falseなら最小化

	Returns:
	    最小基または最大基
	"""
	Q = tuple(sorted(E, key=w, reverse=maximize))
	X = set()
	for qi in Q:
		if independence_oracle(X | {qi}):
			X = X | {qi}
	return X


def worst_out(E, w, basis_superset_oracle, minimize=False):
	"""最悪棄却貪欲法
	計算量は、n:=|E|とし、基拡大集合オラクルの計算量をf(n)としたとき
	O(nlog(n) + nf(n))

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    basis_superset_oracle: 基拡大集合であるかどうかを判定する関数
		minimize: Trueなら最小化、Falseなら最大化

	Returns:
	    最小基または最大基
	"""
	Q = tuple(sorted(E, key=w, reverse=minimize))
	X = E
	for qi in Q:
		if basis_superset_oracle(X - {qi}):
			X = X - {qi}
	return X


def best_in_with_log(E, w, independence_oracle, maximize=False):
	"""最良選択貪欲法をログを残しながら行なう関数
	計算量は、n:=|E|とし、独立性オラクルの計算量をf(n)としたとき
	O(nlog(n) + nf(n))

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    independence_oracle: 独立であるかどうかを判定する関数
		maximize: Trueなら最大化、Falseなら最小化
	
	Returns:
	    最小基または最大基
	"""
	Q = tuple(sorted(E, key=w, reverse=maximize))
	X = set()
	prob_type = "最大化問題" if maximize else "最小化問題"

	print(f"===== {prob_type}に対する最良選択貪欲法 =====")
	print(f"Q = {Q}")
	
	for i, qi in enumerate(Q, 1):
		print("-"*44)
		print(f"X = {X}")
		print(f"次の元: q_{i} = {qi}")
		print("X U {qi} =", X | {qi}, "は独立？:", 'Yes' if independence_oracle(X | {qi}) else 'No')
		if independence_oracle(X | {qi}):
			X = X | {qi}
			print(f"Xが更新されました: X = {X}")
		input("Enterで次のステップ>>")
	print(f"探索終了。得られた解は X = {X} です。")
	print("="*44)

	return X


def worst_out_with_log(E, w, basis_superset_oracle, minimize=False):
	"""最悪棄却貪欲法をログを残しながら行なう関数
	計算量は、n:=|E|とし、基拡大集合オラクルの計算量をf(n)としたとき
	O(nlog(n) + nf(n))

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    basis_superset_oracle: 基拡大集合であるかどうかを判定する関数
		minimize: Trueなら最小化、Falseなら最大化

	Returns:
	    最小基または最大基
	"""
	Q = tuple(sorted(E, key=w, reverse=minimize))
	X = E
	prob_type = "最小化" if minimize else "最大化"

	print(f"===== {prob_type}問題に対する最悪棄却貪欲法 =====")
	print(f"Q = {Q}")
	for i, qi in enumerate(Q, 1):
		print("-"*44)
		print(f"X = {X}")
		print(f"次の元: q_{i} = {qi}")
		print("X - {qi} =", X - {qi}, "は基拡大集合？:", 'Yes' if basis_superset_oracle(X - {qi}) else 'No')
		if basis_superset_oracle(X - {qi}):
			X = X - {qi}
			print(f"Xが更新されました: X = {X}")
		input("Enterで次のステップ>>")
	print(f"探索終了。得られた解は X = {X} です。")
	print("="*44)
	return X