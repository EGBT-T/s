import subprocess

if __name__ == '__main__':
    var = a.py"
    subprocess.run(['python', 'b.py', var])


import sys

if __name__ == '__main__':
    var_from_A = sys.argv[1]
    print("received:", var_from_A)
