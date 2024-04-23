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
    level = kwargs.get('level', 0)
    if level >= DBG_LEVEL:
        print(*args)

DBG_LEVEL = 0

def find_last_height_ge(heights, i, height):
    while i >= 0:
        if heights[i] >= height:
            return i

def main():
    '''
    This is where the task is solved
    '''
    MAX_HEIGHT = int(1e6)
    MAX_QUERIES = int(1e5)
    
    nb_queries = int(input())
    nb_visibles = [None for i in range(nb_queries)]
    
    index_affiche = 0
    for _ in range(nb_queries):
        query = [x for x in input().split(' ')]
        if len(query) == 1:
            print("voir")
        else:
            height = int(query[1])
            debug("coller", height)
            index_affiche += 1
        
        
        debug(index_affiche)


if __name__ == '__main__':
    main()