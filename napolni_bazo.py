#import dj
import atletika.models as atletikamd
import csv

def zapisi_drzave():
    with open('seznam_drzav.csv', 'r', encoding='utf-8') as drzave:
        reader = csv.reader(drzave)
        for row in reader:
            if row != []:
                krat, ime = row
                #print(row)
                d = atletikamd.Drzava(kratica=krat, drzava=ime)
                d.save()

#zapisi = zapisi_drzave()