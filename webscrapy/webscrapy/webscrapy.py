#encoding: utf-8


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
from html_aux import *

# PUCPR - Intranet Login Page
SITE = 'https://sso.pucpr.br/josso/signon/login.do?rf=1&josso_back_to=http://portal.pucpr.br/intranet/josso_security_check'

# My Grades Intranet Page
GradesPage = 'http://portal.pucpr.br/vda/pages/consultanotas/consultanotas.seam'


####################################################
####################################################
# Change here to login into your account
USERNAME = 'YOUR USERNAME HERE'
PASSWORD = 'YOUR PASSWORD HERE'
####################################################
####################################################


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


def GetTableInfo(BSObj, classname):
    """Return Headings and Rows of a table with de classname parameter"""
    if BSObj is not None:
        Table = BSObj.find("table", {"class": classname})
        if Table is None:
            return None, None
        Headings = [th.get_text() for th in Table.find("tr").find_all("th")]
        Rows = []
        for row in Table.findAll("tr")[1:]:
            Rows.append([th.get_text() for th in row.find_all("td")])
        return Headings, Rows
    else:
        print("BSObject is None, load the object using GetBSObject before use this function")
        return None, None

def GenerateHtmlFile(Rows, Nome, TCurso, NCurso):
    file = open("%s Notas.html" % Nome, 'w', encoding = "utf-8")
    message = "" + H_i + Name_i + Nome + Name_e + Info_i + TCurso + Info_e + Info_i + NCurso + Info_e + H_e
    message = message + Table_i
    for row in Rows[9:]:
        message = message + TRow_0
        for info in row:
            message = message + TRow_1 + info + TRow_2
        message = message + TRow_3
    message = message + Table_e + bottom
    file.write(message)   
    file.close()
    print("Done! Check the " + Nome + " Notas.html file")


# Login system used in PUCPR - Intranet system
payload = {
    'josso_cmd': 'login',
    'josso_username': USERNAME,
    'josso_password': PASSWORD
}
#Hidden Layer - Name, Value
#Looking for the username/password class to check the Name and Value
        


    
with requests.session() as c:
    print("Logging into PUCPR - Intranet..")
    c.post(SITE, data=payload)
    print("Getting GradesPage from PUCPR - Intranet..")
    response = c.get(GradesPage)
    bsObj = BeautifulSoup(response.text, "lxml")
    if bsObj is not None:
        idtbody = "consultaNotasAlunoForm:idTableProgramasAprendizagemAluno:tb"
        tableid = "consultaNotasAlunoForm:idTableProgramasAprendizagemAluno"
        tableclass = "rich-table "
        print("Parsing the html file..")
        Headings, Row = GetTableInfo(bsObj, tableclass)
        if (Headings is None) or (Row is None):
            print("\n\nGrades not found! Check your login and password! Please, do not change the URL in the top of the File!\n\n")
        else:
            Nome = bsObj.findAll("input", {"id": "consultaNotasAlunoForm:idTxtNomeAluno"})
            Curso = bsObj.findAll("option", {"value": "1", "selected": "selected"})
            print("Generating the html file..")
            GenerateHtmlFile(Row, Nome[0]['value'], Curso[0].text, Curso[1].text)
        

