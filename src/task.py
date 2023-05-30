

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
    
    position_max = i
    valeur_max = float("-Inf")
    for i in range(n):
        valeur = int(input())
        if valeur > valeur_max:
            position_max = i
        i += 1
    print(position_max)
    


if __name__ == '__main__':
    main()