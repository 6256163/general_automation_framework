# coding=utf-8

from behave.__main__ import main as behave_main

from page_object import PageObject

if __name__ == '__main__':
    behave_main("./features/")