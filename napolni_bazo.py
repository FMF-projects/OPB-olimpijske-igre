from olympic_games.models import Drzava, Disciplina, OlimpijskeIgre, Tekmovalec, Rezultat
import csv
import datetime

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
                igre = row[0]
                disciplina = row[1]
                mesto_iger = igre[:-4]
                leto = int(igre[-4:])
                
                try:
                    d = Disciplina(ime=disciplina)
                    d.save()
                except:
                    disciplina = " "
                
                try:
                    o = OlimpijskeIgre(leto=leto, mesto=mesto_iger)
                    o.save()
                except:
                    mesto_iger = " "

def zapisi_tekmovalce():
    drz = Drzava.objects.all()
    for w in drz:
        print(w.ime)
        t = Tekmovalec(ime=w.ime, drzava=w)
        t.save()
    
    with open('podatki/roj_dan_tekmovalcev.csv', 'r', encoding='utf-8') as tekmovalci:
        reader = csv.reader(tekmovalci)
        for row in reader:
            if row != [] and row[0] != 'ime':
                print(row)
                ime, datum = row
                if datum == "":
                    t = Tekmovalec(ime=ime)
                    t.save()
                else:
                    date = datetime.datetime(int(datum[6:]),int(datum[3:5]),int(datum[0:2]))
                    t = Tekmovalec(ime=ime, rojstvo=date)
                    t.save() 

def zapisi_rezultat():
    tekmovalci = {}
    discipline = {}
    igre = {}
    drzave = {}
    tekm = Tekmovalec.objects.all()
    for x in tekm:
        tekmovalci[x.ime] = x
    disc = Disciplina.objects.all()
    for y in disc:
        discipline[y.ime] = y
    igr = OlimpijskeIgre.objects.all()
    for z in igr:
        igre[z.leto] = z
    drz = Drzava.objects.all()
    for w in drz:
        drzave[w.kratica] = w
    with open('podatki/rezultati.csv', 'r', encoding='utf-8') as rezultati:
        reader = csv.reader(rezultati)
        for row in reader:
            if row != [] and row[0] != 'igre':
                print(row)
                if len(row) == 1:
                    ig, disciplina, mesto, ime, drzava, rezultat = row[0].split(',')[:6]
                else:
                    ig, disciplina, mesto, ime, drzava, rezultat = row
                if mesto == "":
                    mesto = 0
                if ime != "": 
                    t = tekmovalci[ime]
                    d = discipline[disciplina]
                    i = igre[int(ig[-4:])]
                    r = Rezultat(ime=t,disciplina=d, mesto=mesto, rezultat=rezultat, olimpijske_igre=i)
                    r.save()
                else: #imamo skupinsko disciplino
                    ime = drzave[drzava]
                    print(ime)
                    t = tekmovalci[ime.ime]
                    print(t)
                    d = discipline[disciplina]
                    i = igre[int(ig[-4:])]
                    r = Rezultat(ime=t,disciplina=d, mesto=mesto, rezultat=rezultat, olimpijske_igre=i)
                    r.save()

#zapisi_drzave()
#zapisi_tekmovalce()
#zapisi_rezultat()