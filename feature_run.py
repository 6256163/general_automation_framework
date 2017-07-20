import re
import sys
import os

from behave.__main__ import main as behave_main

if __name__ == '__main__':
    # print(os.getcwd())
    # os.chdir(os.path.pardir)
    # print(os.getcwd())
    behave_main("./features/")