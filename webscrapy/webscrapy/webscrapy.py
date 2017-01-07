from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from os import system

SITE = "http://rank.shoryuken.com/rankings/rank/SF5?alltime=true"
SITE2 = "http://www.pythonscraping.com/pages/page3.html"

def CheckSite(url):
    """CheckSite will return the urllib object if the site is available"""
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("Site couldn't be found")
        return None
    return html

def GetTitle(url):
    """GetTitle will return the website's title if they are available"""
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
    """GetBSObject will return the Beatiful Soup Object if the site is available, using the parameter "lxml" """
    site = CheckSite(url)
    if site is not None:
        return BeautifulSoup(site.read(), "lxml")
    else:
        print("Could't create the BS Object")
        return None

#if bsObj is not None:
#    #print(bsObj)
#    Table = bsObj.find("table", {"class":"table table-striped table-hover table-condensed"}) #Aqui ele procura por uma tabela com essa classe
#    headings = [th.get_text() for th in Table.find("tr").find_all("th")] #o find pega a primeira instancia, entao o primeiro find sao os nomes das colunas!
#    #print(headings)
#    Players = []
#    #Como eu nao quero o primeiro tr (headings), eu pego somente os trs apos ele que seriam as linhas da tabela
#    for row in Table.findAll("tr")[1:]: 
#        #Cada linha tem uma informacao para cada coluna, aqui eu simplemente peguei na posicao 2 do vetor que seria o nome do jogador
#        Players.append(row.find_all("td")[2].get_text()) 
#    for player in Players:
#        print(player)


def GetTableInfo(BSObj, classname):
    """Return Headings and Rows of a table with de classname parameter"""
    if BSObj is not None:
        Table = BSObj.find("table", {"class": classname})
        Headings = [th.get_text() for th in Table.find("tr").find_all("th")]
        Rows = []
        for row in Table.findAll("tr")[1:]:
            Rows.append([th.get_text() for th in row.find_all("td")])
        return Headings, Rows
    else:
        print("BSObject is None, load the object using GetBSObject before use this function")
        return None, None

#GetTableInfo(bsObj, "table table-striped table-hover table-condensed")

bsObj = GetBSObject(SITE2)
if bsObj is not None:
    images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    for image in images:
        print(image["src"])

### Get Siblings tags, parents, etc..
#if bsObj is not None:
#    for child in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#        print(child)
#else:
#    print("bsObj is None")

##PAGE 44