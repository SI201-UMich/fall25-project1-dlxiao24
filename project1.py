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
        next(readsv)
        penguin_data = []
        for penguin in readsv:
            d = {}
            d['id'] = penguin[0]
            d['species'] = penguin[1]
            d['island'] = penguin[2]
            d['bill_length_mm'] = penguin[3]
            d['body_mass_g'] = penguin[6]
            penguin_data.append(d)
        return penguin_data
    
def isolate_island(penguin_data, island):
    island_penguin_data = []
    for penguin in penguin_data:
        if penguin['island'] == island:
            island_penguin_data.append(penguin)
    return island_penguin_data

def species_prop(island_penguin_data):
    species_count = {}
    total = 0
    for penguin in island_penguin_data:
        species_count[penguin['species']] = species_count.get(penguin['species'], 0) + 1
        total += 1 
    for key, value in species_count.items():
        species_count[key] = "{:.2%}".format(value / total)
    print(species_count)
    return species_count
    



def main():
    penguins_loaded = load_penguins("penguins.csv")
    penguins_isolated = isolate_island(penguins_loaded, "Dream")
    species_prop(penguins_isolated)

if __name__ == "__main__":
    main()