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
    hights = [0] * MAX_HIGHT
    
    nb_queries = int(input())
    for _ in range(nb_queries):
        query = input()
        
        
    


if __name__ == '__main__':
    main()