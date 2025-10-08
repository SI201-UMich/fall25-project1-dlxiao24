'''
Name: Daniel Xiao
Student ID: 5917 9504
Email: dlxiao@umich.edu
Collaborators: None
'''

import csv
import unittest

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
    return species_count

def avg_mass(island_penguin_data):
    total_mass = 0
    count = 0
    for penguin in island_penguin_data:
        if penguin['body_mass_g'] == 'NA':
            continue
        total_mass += float(penguin['body_mass_g'])
        count += 1
    return "{:.2f}".format(total_mass / count)

def generate_report(species_proportions, avg_body_mass, island):
    with open("Penguin_Report.txt", 'w', newline= '\n') as fhand:
        report = f"Data for {island} island:\nSpecies breakdown: {species_proportions}\nAverage body mass: {avg_body_mass}"
        fhand.write(report)

class TestPenguins(unittest.TestCase):
    def setUp(self):
        self.file = "penguins.csv"
        self.island = "Biscoe"
        self.penguins_loaded = load_penguins(self.file)
        self.penguins_isolated = isolate_island(self.penguins_loaded, self.island)
    
    def test_proportions(self):
        self.assertEqual(species_prop(self.penguins_isolated), {'Adelie': '26.19%', 'Gentoo': '73.81%'})

def main():
    file = "penguins.csv"
    island = "Biscoe"
    penguins_loaded = load_penguins(file)
    penguins_isolated = isolate_island(penguins_loaded, island)
    prop = species_prop(penguins_isolated)
    mass = avg_mass(penguins_isolated)
    generate_report(prop, mass, island)

if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)