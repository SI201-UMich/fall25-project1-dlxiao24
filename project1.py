'''
Name: Daniel Xiao
Student ID: 5917 9504
Email: dlxiao@umich.edu
Collaborators: None
'''




import csv

with open('penguins.csv', newline = '') as penguinfile:
    readsv = csv.reader(penguinfile)
    for line in readsv:
        print(line)

