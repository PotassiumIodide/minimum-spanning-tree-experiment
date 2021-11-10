import src.greedy_algorithm as greedy
from src import independence_oracle
from src import basis_superset_oracle
from src.function import functionize, generalize
from src import dual

def solve_MST_problem(M, weight_function):
    E, D = M
    D_ast = dual.of_bases(E, D) # 基族の双対

    # 重み関数wの一般化とw'の設定
    w = generalize(weight_function)
    w_max = max(w(e) for e in E)
    w_prime = generalize(lambda e: w_max - weight_function(e) + 1)

    # 独立性オラクルの設定
    indep_oracle = independence_oracle.by_bases(D)
    # 基拡大集合オラクルの設定
    bs_oracle = basis_superset_oracle.by_bases(D_ast)

    ans_max_best_in = greedy.best_in_with_log(E, w_prime, indep_oracle, maximize=True)
    ans_min_best_in = greedy.best_in(E, w, indep_oracle)
    ans_max_worst_out = E - greedy.worst_out(E, w, bs_oracle)
    ans_min_worst_out = E - greedy.worst_out(E, w_prime, bs_oracle, minimize=True)

    print(f"最大化問題に対する最良選択貪欲法による解: {ans_max_best_in}")
    print(f"最小化問題に対する最良選択貪欲法による解: {ans_min_best_in}")
    print(f"最大化問題に対する最悪棄却貪欲法による解: {ans_max_worst_out}")
    print(f"最小化問題に対する最悪棄却貪欲法による解: {ans_min_worst_out}")


if __name__ == "__main__":
    E = {1,2,3,4,5,6}
    D = [{1,2,3}, {1,3,4}, {1,3,5}, {2,3,4},{2,3,5}]
    M = (E, D)
    weights = {
        1: 50,
        2: 10,
        3: 32,
        4: 25,
        5:  6,
        6: 28
    }
    w = functionize(weights)

    solve_MST_problem(M, w)