'''
This file contains a bug to illustrate the debugger in the gitpod environment.
'''
# Load tests from the `test1.in` file in the `tests` folder
try:
    from pysoi import *
    load_test('test1')
except:
    pass
def debug(*args, **kwargs):
    level = kwargs.get('level', 1)
    if level <= DBG_LEVEL:
        print(*args)
DBG_LEVEL = 0
def find_last_height_geq(heights, i):
    '''
    >>> heights = [4, 3, 2, 1, 3, 5, 3]
    >>> find_last_height_geq(heights, 0)
    -1
    >>> find_last_height_geq(heights, 1)
    0
    >>> find_last_height_geq(heights, 3)
    2
    >>> find_last_height_geq(heights, 4)
    1
    >>> find_last_height_geq(heights, 5)
    -1
    >>> find_last_height_geq(heights, 6)
    5
    >>>
    '''
    height = heights[i]
    i -= 1
    j = -1
    for j in range(i, -1, -1):
        if heights[j] >= height:
            return j
    return -1
def main():
    '''
    This is where the task is solved
    '''
    MAX_HEIGHT = int(1e6)
    MAX_QUERIES = int(1e5)
    
    nb_queries = int(input())
    nb_visibles = [0 for i in range(nb_queries)]
    heights = [0 for i in range(nb_queries)]
    
    index_affiche = 0
    for _ in range(nb_queries):
        query = [x for x in input().split(' ')]
        if len(query) == 1:
            debug("query")
            print(nb_visibles[index_affiche - 1])
        else:
            height = int(query[1])
            debug("coller", height)
            heights[index_affiche] = height
            index_last_geq = find_last_height_geq(heights, index_affiche)
            debug("visibles", nb_visibles)
            debug("heights", heights)
            debug("last geq index", index_last_geq)
            if index_last_geq == -1:
                nb_visibles[index_affiche] = 1
            elif heights[index_last_geq] == height:
                nb_visibles[index_affiche] = nb_visibles[index_last_geq]
            elif heights[index_last_geq] > height:
                nb_visibles[index_affiche] = nb_visibles[index_last_geq] + 1
            
            index_affiche += 1
        
        
        debug("index_affiche", index_affiche)
        debug("-----------")
if __name__ == '__main__':
    main()
    
    
try:
    import doctest
    doctest.testmod()
except:
    print("Impossible de lancer les doctests")