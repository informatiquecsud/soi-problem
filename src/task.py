'''
This file contains a bug to illustrate the debugger in the gitpod environment.
'''

# Load tests from the `test1.in` file in the `tests` folder
try:
    from pysoi import *
    load_test('test1')
except:
    pass
    

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
            print("coller", index_affiche)
            index_affiche += 1
        
        
    


if __name__ == '__main__':
    main()