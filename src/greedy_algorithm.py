def best_in(E, w, independence_judger, maximize=False):
	"""最良選択貪欲法

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    independence_judger: 独立であるかどうかを判定する関数
		maximize: Trueなら最大化、Falseなら最小化
	"""
	Q = sorted(E, key=w, reverse=maximize)
	X = set()
	for qi in Q:
		if independence_judger(X | {qi}):
			X = X | {qi}
	return X


def best_in_with_log(E, w, independence_judger, maximize=False):
	"""最良選択貪欲法をログを残しながら行なう関数

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    independence_judger: 独立であるかどうかを判定する関数
		maximize: Trueなら最大化、Falseなら最小化
	"""
	print("===== 最良選択貪欲法 =====")
	Q = sorted(E, key=w, reverse=maximize)
	X = set()
	print(f"Q = {Q}")
	for i, qi in enumerate(Q, 1):
		print("-"*25)
		print(f"X = {X}")
		print(f"次の元: q_{i} = {qi}")
		print("X U {qi} =", X | {qi}, "は独立？:", 'Yes' if independence_judger(X | {qi}) else 'No')
		if independence_judger(X | {qi}):
			X = X | {qi}
			print(f"Xが更新されました: X = {X}")
		input("Enterで次のステップ>>")
	print(f"探索終了。得られた解は X = {X} です。")
	return X


def worst_out(E, w, basis_superset_judger, minimize=False):
	"""最悪棄却貪欲法

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    basis_superset_judger: 基拡大集合であるかどうかを判定する関数
		minimize: Trueなら最小化、Falseなら最大化
	"""
	Q = sorted(E, key=w, reverse=minimize)
	X = E
	for qi in Q:
		if basis_superset_judger(X - {qi}):
			X = X - {qi}
	return X


def worst_out_with_log(E, w, basis_superset_judger, minimize=False):
	"""最悪棄却貪欲法をログを残しながら行なう関数

	Args:
		M: 独立性システム
		w: 重み関数(コスト関数) w: E → R+
	    basis_superset_judger: 基拡大集合であるかどうかを判定する関数
		minimize: Trueなら最小化、Falseなら最大化
	"""
	print("===== 最悪棄却貪欲法 =====")
	Q = sorted(E, key=w, reverse=minimize)
	X = E
	print(f"Q = {Q}")
	for i, qi in enumerate(Q, 1):
		print("-"*25)
		print(f"X = {X}")
		print(f"次の元: q_{i} = {qi}")
		print("X - {qi} =", X - {qi}, "は基拡大集合？:", 'Yes' if basis_superset_judger(X - {qi}) else 'No')
		if basis_superset_judger(X - {qi}):
			X = X - {qi}
			print(f"Xが更新されました: X = {X}")
		input("Enterで次のステップ>>")
	print(f"探索終了。得られた解は X = {X} です。")
	return X