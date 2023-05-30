
import sys
import os

TEST_EXTENSION = '.in'

def load_soi_test(filename, testdir='tests', extension=TEST_EXTENSION):
    files = os.listdir(path=testdir)

    for f in files:
        f = os.path.join(testdir, f)
        if os.path.isfile(f) and f.endswith(extension):
            name = f.split(extension)[0]
            print(f"Found test {name}")

    # Redirecting the selected file to standard input for debugging purposes
    sys.stdin = open(os.path.join(testdir, f"{filename}.in"), "r")
            
def load_soi_test1(filename, extension=TEST_EXTENSION):
    file_path = os.path.dirname(__file__)
    os.chdir(file_path)
    test_dir = os.path.join('..', 'tests')

    files = os.listdir(path=test_dir)

    for f in files:
        f = os.path.join(test_dir, f)
        if os.path.isfile(f) and f.endswith(extension):
            name = f.split(extension)[0]
            print(f"Found test {name}")
        
    test_to_run = int(input("Test to run (just enter the test number): "))
