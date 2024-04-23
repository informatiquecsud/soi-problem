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
    
    nb_queries = int(input())
    for _ in range(12):
        query = input()
        
    


if __name__ == '__main__':
    main()