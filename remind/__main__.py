import subprocess
import os
import sys 
from task import *

def main():
    arg = sys.argv
    task1 = Task(arg[1])
    task1.notify_Desktop()

if __name__ == '__main__':
    main()
