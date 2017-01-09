from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import re
from os import system

SITE = "http://rank.shoryuken.com/rankings/rank/SF5?alltime=true"
SITE2 = "http://www.pythonscraping.com/pages/page3.html"
SITE3 = 'https://sso.pucpr.br/josso/signon/login.do?rf=1&josso_back_to=http://portal.pucpr.br/intranet/josso_security_check'

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

#if bsObj is not None:
#    images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
#    for image in images:
#        print(image["src"])

### Get Siblings tags, parents, etc..
#if bsObj is not None:
#    for child in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#        print(child)
#else:
#    print("bsObj is None")

##PAGE 44

USERNAME = 'RARARAr'
PASSWORD = 'RARARAR'

payload = {
    'josso_cmd': 'login',
    'josso_username': USERNAME,
    'josso_password': PASSWORD
}
#Hidden Layer - Name, Value
#Looking for the username/password class to check the Name and Value
SITE4 = 'http://criticalart.pythonanywhere.com/admin/login/?next=/admin/'

# Home page Intranet
# 'http://portal.pucpr.br/intranet/pages/main.seam?cid=29680#'

# My notes Intranet
Mynotes = 'http://portal.pucpr.br/intranet/pages/carregarConteudo.seam?pagina=http://intranetportal.pucpr.br/intv3_aluno_index.php5?recurso=INTV3.ALUNO.PAGINA_INICIAL#'

# 'http://criticalart.pythonanywhere.com/admin/Player/player/'
with requests.session() as c:
    c.post(SITE3, data=payload)
    response = c.get(Mynotes)
    print(response.headers)
    print(response.text)


