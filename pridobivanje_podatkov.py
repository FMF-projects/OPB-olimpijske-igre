import orodja
import re
import unicodedata
import os
from pathlib import Path


leta = ["/rio-2016", "/london-2012", "/beijing-2008", "/athens-2004", 
        "/sydney-2000", "/atlanta-1996", "/barcelona-1992", "/seoul-1988",
        "/los-angeles-1984", "/moscow-1980", "/montreal-1976", "/munich-1972",
        "/mexico-1968", "/tokyo-1964", "/rome-1960", "/melbourne-stockholm-1956",
        "/helsinki-1952", "/london-1948", "/berlin-1936", "/los-angeles-1932",
        "/amsterdam-1928", "/paris-1924", "/antwerp-1920", "/stockholm-1912",
        "/london-1908", "/st-louis-1904", "/paris-1900", "/athens-1896"]
sport = "/athletics"
discipline = ["/10000m-men", "/100m-men", "/110m-hurdles-men", "/1500m-men",
              "/200m-men", "/20km-walk-men", "/3000m-steeplechase-men",
              "/400m-hurdles-men", "/400m-men", 
              
              "/4x100m-relay-men", "/4x400m-relay-men", 
              "/5000m-men", "/50km-walk-men", "/800m-men",
              "/decathlon-men", "/discus-throw-men", "/hammer-throw-men",
              "/high-jump-men", "/javelin-throw-men", "/long-jump-men",
              "/marathon-men", "/pole-vault-men", "/shot-put-men", "/triple-jump-men",

              "/10000m-women", "/100m-hurdles-women", "/100m-women", 
              "/1500m-women", "/200m-women", "/20km-race-walk-women",
              "/3000m-steeplechase-women", "/400m-hurdles-women", "/400m-women",
              "/4x100m-relay-women", "/4x400m-relay-women", 
              "/5000m-women",
              "/800m-women", "/discus-throw-women", "/hammer-throw-women",
              "/heptathlon-women", "/high-jump-women", "/javelin-throw-women",
              "/long-jump-women", "/marathon-women", "/pole-vault-women",
              "/shot-put-women", "/triple-jump-women"]
mostva = ["/4x100m-relay-men", "/4x100m-relay-women", "/4x400m-relay-men", "/4x400m-relay-women"]
osnovni_naslov = "https://www.olympic.org"


def podatki_posameznik(datoteka, olimpijske, disciplina):

        #with open(datoteka, encoding='utf-8') as f:
        with open(str(datoteka), encoding='utf-8') as f:
            vsebina = f.read()

            for tekmovalec in re.finditer(
                r'<tr>.+?<td class="col1">(?P<mesto>.+?)</td>.+?<td class="col2">'
                r'.+?<a href="/(?P<ime>.+?)">.+?<span class="picture">'
                #r'.+?<strong .*?class="name">(?P<ime>.+?)</strong>'
                r'.+?<span.*?>(?P<drzava>\D{3})</span>'
                r'.+?<td class="col3">(?P<rezultat>.+?)</td>.+?</tr>'
            ,vsebina, flags=re.DOTALL):
                
                mesto = tekmovalec.group('mesto')
                x = re.search('\d+', mesto)
                if x:
                    mesto = x.group()
                else:
                    if re.search('G', mesto):
                        mesto = '1'
                    elif re.search('S', mesto):
                        mesto = '2'
                    elif re.search('B', mesto):
                        mesto = '3'
                    else:
                        mesto = ''  

                ime = tekmovalec.group('ime')
                ime = ime.replace("-", " ")
                ime = ime.title()

                drzava = tekmovalec.group('drzava')

                rezultat = tekmovalec.group('rezultat')
                rezultat = rezultat.strip()
                rezultat = rezultat.replace("\n", "")

                igre = olimpijske[1:]
                igre = igre.replace("-", " ")
                igre = igre.capitalize()

                # za vsakega nastopajočega ustvarimo slovar
                nastop = {}
                nastop['igre'] = igre
                nastop['disciplina'] = disciplina
                nastop['mesto'] = mesto
                nastop['ime'] = ime
                nastop['drzava'] = drzava
                nastop['rezultat'] = rezultat
                rezultati.append(nastop)
                # print(rezultati)
                sez.add(tekmovalec.group('ime'))
                # print(len(sez))

def posameznik_rojstni_dan(datoteka):

    with open(str(datoteka), encoding='utf-8') as f:
        vsebina = f.read()

        for tekmovalec in re.finditer(
            r'<h1 itemprop="name">(?P<ime>.+?)</h1>'
            r'.+?<div class="frame">'
            r'.+?<strong class="title">Born</strong>'
            r'(?P<datum>.+?)'
            r'</div>.+?</li>'
            r'.+?<strong class="title">.+?</strong>'
            r'.+?<div class="switcher">'
        , vsebina, flags=re.DOTALL):

            ime = tekmovalec.group('ime')
            ime = ime.replace("\n", "")
            ime = ime.title()

            datum = tekmovalec.group('datum')
            datum = datum.replace("\n", "")

            #print(ime, datum)
            nastopajoci = {}
            nastopajoci['ime'] = ime
            nastopajoci['datum'] = datum
            tekmovalci.append(nastopajoci)
            #print(tekmovalci)

        for drzava in re.finditer(
            r'<div class="profile-row">'
            r'.+?<span>(?P<kratica>.+?)</span>'
            r'.+?<ul class="medal-box">'
            r'.+?<div class="frame">'
            r'.+?<strong class="title">Country </strong>'
            r'.+?<a itemprop="url" href="/.+?">(?P<drzava>.+?)</a>'
            r'.+?<div class="text-box">'
            r'.+?<div class="switcher">'
        , vsebina, flags=re.DOTALL):

            kratica = drzava.group('kratica')
            drzava = drzava.group('drzava')

            drzave_s_kratico = {}
            drzave_s_kratico['kratica'] = kratica
            drzave_s_kratico['drzava'] = drzava
            drzave.append(drzave_s_kratico)

def seznam_tekmovalcev(datoteka):

    #with open(datoteka, encoding='utf-8') as f:
    with open(str(datoteka), encoding='utf-8') as f:
        vsebina = f.read()

        for tekmovalec in re.finditer(
                r'<tr>.+?<td class="col1">(?P<mesto>.+?)</td>.+?<td class="col2">'
                r'.+?<a href="/(?P<ime>.+?)">.+?<span class="picture">'
                # r'.+?<strong .*?class="name">(?P<ime>.+?)</strong>'
                r'.+?<span.*?>(?P<drzava>\D{3})</span>'
                r'.+?<td class="col3">(?P<rezultat>.+?)</td>.+?</tr>'
                , vsebina, flags=re.DOTALL):

            html.append(tekmovalec.group('ime'))
    return html

def podatki_skupine(datoteka, olimpijske, disciplina):

        #with open(datoteka, encoding='utf-8') as f:
        with open(str(datoteka), encoding='utf-8') as f:
            vsebina = f.read()

            for tekmovalec in re.finditer(
                r'<tr>.+?<td class="col1">.+?<span class=".+?">(?P<mesto>.+?)</span>.+?<td class="col2">'
                r'.+?<strong class="name">(?P<ime>.+?)</strong>'
                r'.+?<td class="col3">(?P<rezultat>.+?)?</td>.+?</tr>'
            ,vsebina, flags=re.DOTALL):
                
                mesto = tekmovalec.group('mesto')
                if len(mesto) > 5:
                    mesto = ""
                elif mesto == 'G':
                    mesto = '1.'
                elif mesto == 'S':
                    mesto = '2.'
                elif mesto == 'B':
                    mesto = '3.'
                mesto = mesto.strip(".")
                mesto = mesto.strip("\n")    

                ime = tekmovalec.group('ime')
                ime = ime.replace("-", " ")
                ime = ime.title()

                rezultat = tekmovalec.group('rezultat')
                rezultat = rezultat.strip()
                rezultat = rezultat.replace("\n", "")

                igre = olimpijske[1:]
                igre = igre.replace("-", " ")
                igre = igre.capitalize()

                # za vsakega nastopajočega ustvarimo slovar
                nastop = {}
                nastop['igre'] = igre
                nastop['disciplina'] = disciplina
                nastop['mesto'] = mesto
                nastop['ime'] = ime
                nastop['drzava'] = "" #TODO dodaj kratico
                nastop['rezultat'] = rezultat
                rezultati.append(nastop)

def prenesi_html():
     for olimpijske in leta:
        for disciplina in discipline:
             naslov = osnovni_naslov + olimpijske + sport + disciplina
             datoteka = "rezultati_{}_{}.html".format(olimpijske, disciplina)
             orodja.shrani(naslov, datoteka)

def prenesi_html_tekmovalca():
    for olimpijske in leta:
        for disc in discipline:

            disciplina = disc

            mapa = Path("rezultati_{}_".format(olimpijske))
            # print(mapa)
            dat = mapa / "{}.html".format(disc[1:])
            #print(dat)


            if disc not in mostva:
                for tekmovalec in seznam_tekmovalcev(dat):
                    #print(tekmovalec)
                    naslov = osnovni_naslov + "/" + tekmovalec
                    #print(naslov)
                    datoteka = "{}.html".format(tekmovalec)
                    pot = os.path.join("tekmovalci", datoteka)
                    orodja.shrani(naslov, pot)

def preberi_podatke():

    for olimpijske in leta:
        for disc in discipline:

            disciplina = disc
            disciplina = disciplina.replace("-", " ")
            disciplina = disciplina.replace("/", "")

            mapa = Path("rezultati_{}_".format(olimpijske))
            dat = mapa / "{}.html".format(disc[1:])

            if disc in mostva:
                podatki_skupine(dat, olimpijske, disciplina)
            else:
                podatki_posameznik(dat, olimpijske, disciplina)
            
            #print(olimpijske, disciplina)

    #cwd = os.getcwd()
    #print(cwd)
    #print(sez)
    for tekmovalec in list(sez):
        dat = Path("tekmovalci")
        pot = dat / "{}.html".format(tekmovalec)
        posameznik_rojstni_dan(pot)


rezultati = []
tekmovalci = []
sez = set()
html = []
drzave = []

#prenesi_html()
#prenesi_html_tekmovalca()

preberi_podatke()

#orodja.zapisi_tabelo(rezultati, ['igre', 'disciplina', 'mesto', 'ime', 'drzava', 'rezultat'], 'rezultati.csv')
#print("Zapis tabele tekmovalci.")
#orodja.zapisi_tabelo(tekmovalci, ['ime', 'datum'], 'tekmovalci.csv')
#print("Zapis tabele seznam_drzav.")
#orodja.zapisi_tabelo(drzave, ['kratica', 'drzava'], 'seznam_drzav.csv')