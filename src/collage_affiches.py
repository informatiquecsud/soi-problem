"""
This file contains a bug to illustrate the debugger in the gitpod environment.
"""

# Load tests from the `test1.in` file in the `tests` folder

try:
    from pysoi import *

    load_test("test1")
except:
    pass

import sys
input = sys.stdin.readline

def debug(*args, **kwargs):
    level = kwargs.get("level", 1)
    if level <= DBG_LEVEL:
        print(*args)


DBG_LEVEL = 0

def find_last_height_geq(heights, i, last_geq):
    """
    """
    height = heights[i]
    j = i - 1

    while j >= 0:
        if heights[j] >= height:
            last_geq[i] = j
            return j
        else:
            j = last_geq[j]

    return -1


def main():
    """
    This is where the task is solved
    """
    MAX_HEIGHT = int(1e6)
    MAX_QUERIES = int(1e5)

    nb_queries = int(input())
    nb_visibles = [0 for i in range(nb_queries)]
    heights = [0 for i in range(nb_queries)]
    last_geq = [i - 1 for i in range(nb_queries)]

    index_affiche = 0
    for _ in range(nb_queries):
        query = [x for x in input().split(" ")]
        if len(query) == 1:
            sys.stdout.write(str(nb_visibles[index_affiche - 1]) + "\n")
        else:
            height = int(query[1])

            heights[index_affiche] = height
            index_last_geq = find_last_height_geq(heights, index_affiche, last_geq)
            
            if index_last_geq == -1:
                nb_visibles[index_affiche] = 1
            elif heights[index_last_geq] == height:
                nb_visibles[index_affiche] = nb_visibles[index_last_geq]
            elif heights[index_last_geq] > height:
                nb_visibles[index_affiche] = nb_visibles[index_last_geq] + 1

            index_affiche += 1



if __name__ == "__main__":
    main()


try:
    import doctest

    doctest.testmod()
except:
    print("Impossible de lancer les doctests")
