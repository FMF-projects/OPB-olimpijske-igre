import orodja
import re
import unicodedata
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
              
              #"/4x100m-relay-men", "/4x400m-relay-men", 
              "/5000m-men", "/50km-walk-men", "/800m-men",
              "/decathlon-men", "/discus-throw-men", "/hammer-throw-men",
              "/high-jump-men", "/javelin-throw-men", "/long-jump-men",
              "/marathon-men", "/pole-vault-men", "/shot-put-men", "/triple-jump-men",

              "/10000m-women", "/100m-hurdles-women", "/100m-women", 
              "/1500m-women", "/200m-women", "/20km-race-walk-women",
              "/3000m-steeplechase-women", "/400m-hurdles-women", "/400m-women",
              #"/4x100m-relay-women", "/4x400m-relay-women", 
              "/5000m-women",
              "/800m-women", "/discus-throw-women", "/hammer-throw-women",
              "/heptathlon-women", "/high-jump-women", "/javelin-throw-women",
              "/long-jump-women", "/marathon-women", "/pole-vault-women",
              "/shot-put-women", "/triple-jump-women"]
mostva = ["/4x100m-relay-men", "/4x100m-relay-women"]
osnovni_naslov = "https://www.olympic.org"


def podatki_posameznik(datoteka, olimpijske, disciplina):

        with open(datoteka, encoding='utf-8') as f:
            vsebina = f.read()

            for tekmovalec in re.finditer(
                r'<tr>.+?<td class="col1">(?P<mesto>.+?)</td>.+?<td class="col2">'
                r'.+?<a href="/(?P<ime>.+?)">.+?<span class="picture">'
                #r'.+?<strong .*?class="name">(?P<ime>.+?)</strong>'
                r'.+?<span.*?>(?P<drzava>\D{3})</span>'
                r'.+?<td class="col3">(?P<rezultat>.+?)</td>.+?</tr>'
            ,vsebina, flags=re.DOTALL):
                
                mesto = tekmovalec.group('mesto')
                x = re.search('\d', mesto)
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

def podatki_skupine(datoteka, olimpijske, disciplina):

        with open(datoteka, encoding='utf-8') as f:
            vsebina = f.read()

            for tekmovalec in re.finditer(
                r'<tr>.+?<td class="col1">.+?<span class=".+?">(?P<mesto>.+?)</span>.+?<td class="col2">'
                r'.+?<strong class="name">(?P<ime>.+?)</strong>'
                r'.+?<td class="col3">(?P<rezultat>.+?)</td>.+?</tr>'
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
                nastop['drzava'] = ""
                nastop['rezultat'] = rezultat
                rezultati.append(nastop)

def prenesi_html():
     for olimpijske in leta:
        for disciplina in discipline:
             naslov = osnovni_naslov + olimpijske + sport + disciplina
             datoteka = "rezultati_{}_{}.html".format(olimpijske, disciplina)
             orodja.shrani(naslov, datoteka)

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
            
            print(olimpijske, disciplina)


rezultati = []
#prenesi_html()
preberi_podatke()
#orodja.zapisi_tabelo(rezultati, ['igre', 'disciplina', 'mesto', 'ime', 'drzava', 'rezultat'], 'rezultati.csv')
