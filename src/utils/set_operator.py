from functools import reduce
from itertools import chain, combinations
from operator import or_
from typing import Any, Iterable, TypeVar

T = TypeVar('T')

def powset(E: set[T]) -> list[set[T]]:
    """Return the power set, a set of all subsets, of a given set E
    Arguments:
        E: {set} - a ground set
    Returns:
        {list[set]} - the power set of a given set E.
    """
    return [*map(set, chain.from_iterable(combinations(E, r) for r in range(len(E)+1)))]