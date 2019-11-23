#! /usr/bin/python3
# coding:utf-8

import os

f = open("book_chapter.txt", "r")
f1= open("book_chapter_c.txt", encoding='utf-8', mode = "r")
line = f.readline()
with open("book_chapter.txt", encoding='utf-8', mode = "r") as f:
    for line in f:
        line1=f1.readline()
        #line1.encode().decode('utf-8')
        print(line1)
        print(line)