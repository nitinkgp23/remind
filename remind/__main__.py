import subprocess
import os
import sys 
from task import *

def main():
    arg = sys.argv
    task1 = Task(arg[1],arg[2])
    task1.schedule()

if __name__ == '__main__':
    main()
