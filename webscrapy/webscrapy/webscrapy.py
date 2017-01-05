from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from os import system

SITE = "http://rank.shoryuken.com/rankings/rank/SF5?alltime=true"

def CheckSite(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("Site couldn't be found")
        return None
    return html

def GetTitle(url):
    site = CheckSite(url)
    if site is not None:
        try:
            bsObj = BeautifulSoup(site.read(), "lxml")
            title = bsObj.body.h1
        except AttributeError as e:
            return None
        return title
    return None

def GetBSObject(url):
    site = CheckSite(url)
    if site is not None:
        return BeautifulSoup(site.read(), "lxml")
    else:
        print("Could't create the BS Object")
        return None

bsObj = GetBSObject(SITE)
if bsObj is not None:
    #print(bsObj)
    Table = bsObj.find("table", {"class":"table table-striped table-hover table-condensed"}) #Aqui ele procura por uma tabela com essa classe
    headings = [th.get_text() for th in Table.find("tr").find_all("th")] #o find pega a primeira instancia, entao o primeiro find sao os nomes das colunas!
    #print(headings)
    Players = []
    #Como eu nao quero o primeiro tr (headings), eu pego somente os trs apos ele que seriam as linhas da tabela
    for row in Table.findAll("tr")[1:]: 
        #Cada linha tem uma informacao para cada coluna, aqui eu simplemente peguei na posicao 2 do vetor que seria o nome do jogador
        Players.append(row.find_all("td")[2].get_text()) 
    for player in Players:
        print(player)
