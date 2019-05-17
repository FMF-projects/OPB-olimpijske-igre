#import dj
from olympic_games.models import Drzava
import csv

def zapisi_drzave():
    with open('seznam_drzav.csv', 'r', encoding='utf-8') as drzave:
        reader = csv.reader(drzave)
        for row in reader:
            if row != []:
                krat, ime = row
                #print(row)
                d = Drzava(kratica=krat, ime=ime)
                d.save()

zapisi_drzave()