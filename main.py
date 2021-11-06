import src.greedy_algorithm as greedy
from src import independence_judger
from src import basis_superset_judger
from src.function import functionize, generalize
from src import dual

def solve_MST_problem(M, w):
    E, D = M
    judger = independence_judger.by_bases(D)
    ans = greedy.best_in(E, w, judger)
    print(f"最良選択貪欲法による解: {ans}")

    D_ast = dual.of_bases(E, D)
    # print(f"D* = {D_ast}")
    judger = basis_superset_judger.by_bases(D_ast)
    ans = E - greedy.worst_out(E, w, judger)
    print(f"最悪棄却貪欲法による解: {ans}")

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
    w = generalize(functionize(weights))

    solve_MST_problem(M, w)