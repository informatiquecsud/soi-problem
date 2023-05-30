

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
    
    n = int(input())
    
    i = 0
    valeur_max = float("-Inf")
    for _ in range(n):
        valeur = int(input())
        i += 1
        
    


if __name__ == '__main__':
    main()