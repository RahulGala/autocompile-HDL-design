#!/usr/bin/python

import os
import re
import sys
import subprocess

def main():
    for i in range(1,11):
        s= "vcs +v2k and_{}.v | tee report_{}".format(i,i)
        subprocess.call(s,shell=True)
        
if __name__ == '__main__':
    main()
