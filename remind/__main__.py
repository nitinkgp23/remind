import subprocess
import os
import sys 
from task import *

def main():
    arg = sys.argv
    if (len(arg)==1):
        task1 = Task()
    elif(len(arg)==2):
        task1 = Task(arg[1])
    elif(len(arg)==3):
        task1 = Task(arg[1],arg[2])
    elif(len(arg)==4):
        task1 = Task(arg[1],arg[2],arg[3])

        
    task1.schedule()

if __name__ == '__main__':
    main()
