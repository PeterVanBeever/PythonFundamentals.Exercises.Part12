from typing import List, Dict, Set, Callable
import enum
from typing import Callable,Dict #added
from enum import Enum #added

class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Uses a parity based generator to create a lsit 
    of numbers based on even or odd numbers.

    :param start:
    :param stop:
    :param parity:
    :return:
    """ #updated docstring for clarity
    
    # odd
    if parity == Parity.ODD:
        #if divisible by 2 (not odd)
        return [i for i in range(start, stop) if i  % 2 != 0]
    # even
    elif parity == Parity.EVEN:
        return [i for i in range(start, stop) if i % 2 == 0]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Uses a callable (function) to return a dictionary of numbers
    Keys are integers from start to stop
    Strategy defines how to calculate the values for each key
    Anonymous lambda returns square of the number

    :param start:
    :param stop:
    :param strategy:
    :return:
    """

    return {i: strategy(i) for i in range(start, stop)}

    pass


def gen_set(val_in: str) -> Set[str]:
    """
    Creates a set of uppercase letters of the string's lowercase letters

    :param val_in:
    :return:
    """

    return {char.upper() for char in val_in if char.islower()}


    pass
