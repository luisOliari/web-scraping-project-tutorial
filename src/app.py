pip install pandas sqlite3 requests
pip install pandas

import pandas as pd
import requests 
import sqlite3
from bs4 import BeautifulSoup

#html_data
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text

#soup
soup = BeautifulSoup(html_data,"html.pars
tablas = soup.findAll("table")

# con Crl + F buscamos la palabra clave revenue
tablas 

for i, tabla in enumerate(tablas):
    if ("Tesla Quarterly Revenue" in str(tabla)): 
        indice_que_busco = i 
#enumerate me asigna un índice y el contenido que encuentra
df = pd.DataFrame(columns=["date","revenue"])

tablas[indice_que_busco]

for fila in tablas[indice_que_busco].tbody.find_all("tr"):
    datos= fila.find_all("td")

datos

datos[0]

datos[1].text

for fila in tablas[indice_que_busco].tbody.find_all("tr"):
    datos= fila.find_all("td")
    if len(datos)>0:
        fecha=datos[0].text
        revenue=datos[1].text.replace("$","").replace(",","")
        df = df.append({"date":fecha,"revenue":revenue},ignore_index=True)
df.tail()

df=df[df["revenue"]!=""]

df.tail()

df.head(5)




