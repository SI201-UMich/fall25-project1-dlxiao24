'''
Name: Daniel Xiao
Student ID: 5917 9504
Email: dlxiao@umich.edu
Collaborators: None
'''

import csv
def load_penguins(csvfile):
    with open(csvfile, newline = '') as penguinfile:
        readsv = csv.reader(penguinfile)
        for line in readsv:
            print(line)

def main():
    load_penguins("penguins.csv")

if __name__ == "__main__":
    main()