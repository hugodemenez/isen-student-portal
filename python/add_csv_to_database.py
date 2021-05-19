
import csv

#On va lire le fichier structure.csv 
with open('08c-Projet_N3_test_structure.csv') as structure_order_csv_file:
    spamreader2 = csv.DictReader(structure_order_csv_file, delimiter=";")
    #On tri les donnes du fichier csv dans un dictionnaire trié par selection puis chapitre puis activite pui sous activite
    row_sorted_list2 = sorted(spamreader2, key=lambda row:(row['Selection'],row['Chapitre'],row['Activite'],row['Sous_activite']), reverse=False)