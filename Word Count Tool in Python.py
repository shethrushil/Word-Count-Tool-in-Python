# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:29:43 2023

@author: rushilsheth
"""

def word_count(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        words = text.split()
        return len(words)

file_name = input("Enter the file name: ")
count = word_count(file_name)
print("Number of words in the file: ", count)
