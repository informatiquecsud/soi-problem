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

def main():
    '''
    This is where the task is solved
    '''
    MAX_HIGHT = int(1e6)
    
    
    hights = [[] for _ in range(MAX_HIGHT)]
    
    nb_queries = int(input())
    
    index_affiche = 0
    for _ in range(nb_queries):
        query = [x for x in input().split(' ')]
        if len(query) == 1:
            print("voir")
        else:
            hight = int(query[1])
            hights[hight].append(index_affiche)
            debug("coller", hight)
            debug(hights[hight])
            index_affiche += 1
        
        
        debug(index_affiche)
    debug(hights)


if __name__ == '__main__':
    main()