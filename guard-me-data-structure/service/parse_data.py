import os
import shutil
import codecs
import csv
from unidecode import unidecode

csv_path = '../../data/'

def parse():
    print("Parsing...")
    with codecs.open(csv_path, 'r', encoding='iso-8859-1') as lines:
        for line in lines:
            #row = [r[1:-1] for r in line[:-1].split(';')]
            try:
                row = list(csv.reader([line], delimiter=';'))[0]
            except Exception as e:
                print(line)
                print(e)
                cur = conn.cursor()
                continue
            print(line)
            print(row)

