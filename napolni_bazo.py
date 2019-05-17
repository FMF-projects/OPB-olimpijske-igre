from olympic_games.models import Drzava, Disciplina, OlimpijskeIgre, Tekmovalec
import csv

def zapisi_drzave():
    with open('podatki/seznam_drzav.csv', 'r', encoding='utf-8') as drzave:
        reader = csv.reader(drzave)
        for row in reader:
            if row != [] and row[0] != 'kratica':
                krat, ime = row
                d = Drzava(kratica=krat, ime=ime)
                d.save()

def zapisi_discipline_in_olimpijske():
    with open('podatki/rezultati.csv', 'r', encoding='utf-8') as rezultati:
        reader = csv.reader(rezultati)
        for row in reader:
            if row != [] and row[0] != 'igre':
                igre, disciplina, mesto, ime, drzava, rezultat = row
                d = Disciplina(ime=disciplina)
                mesto_iger = igre[:-4]
                leto = int(igre[-4:])
                o = OlimpijskeIgre(leto=leto, mesto=mesto_iger)
                d.save()
                o.save()

def zapisi_tekmovalce():
    with open('podatki/rezultati.csv', 'r', encoding='utf-8') as rezultati, open('podatki/roj_dan_tekmovalcev.csv', 'r', encoding='utf-8') as roj_dan:
        reader1 = csv.reader(rezultati)
        reader2 = csv.reader(roj_dan)
        for row1 in reader1:
            if row1 != []:
                igre1, disciplina1, mesto1, ime1, drzava1, rezultat1 = row1
                for row2 in reader2:
                    if row2 != []:
                        ime2, datum2 = row2
                        if ime1 == ime2:
                            if type(ime1[:-1]) == int:
                                t = Tekmovalec(ime=ime1[:-1], drzava=drzava1, rojstvo=datum2, mesto=mesto1, rezultat=rezultat1, olimpijske_igre=igre1)
                                t.save
                            else:
                                t = Tekmovalec(ime=ime1, drzava=drzava1, rojstvo=datum2, mesto=mesto1, rezultat=rezultat1, olimpijske_igre=igre1)
                                t.save

zapisi_drzave()
zapisi_discipline_in_olimpijske()
#zapisi_tekmovalce()

