import sys
import os

TEST_EXTENSION = ".in"


def load_test(filename, testdir="tests", extension=TEST_EXTENSION, debug=False):
    # Redirecting the selected file to standard input for debugging purposes
    sys.stdin = open(os.path.join(testdir, f"{filename}.in"), "r")
    sys.stdout = open(os.path.join(testdir, f"{filename}.run.out"), "w")
