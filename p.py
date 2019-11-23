#! /usr/bin/python3
# coding: utf-8

import os
rootdir = "D:/学习书籍/mybook/book"

for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:
        print("目录名: ", dirname)

    print("\n\n")

    for filename in filenames:
        print("(book/",filename+")")