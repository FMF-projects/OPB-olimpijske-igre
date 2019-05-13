from olympic_games.models import Disciplina, OlimpijskeIgre, Drzava, Tekmovalec
import csv

def zapisi_drzave():
    with open('seznam_drzav.csv', 'r', encoding='utf8') as drzave:
        reader = csv.reader(drzave)
        for row in reader:
            if row != []:
                krat, ime = row
                d = drzava(kratica=krat, drzava=ime)
                d.save()

