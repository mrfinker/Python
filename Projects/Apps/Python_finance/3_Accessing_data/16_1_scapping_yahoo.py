import pandas as pd
import requests

url_link = "https://finance.yahoo.com/quote/TSLA/profile"
r = requests.get(url_link, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})

data = pd.read_html(r.text)
print(data[0])
print()


#Ce code provoquera une erreur, car Yahoo vérifie le demandeur et nécessite un en-tête valide.
#data = pd.read_html("https://finance.yahoo.com/quote/TSLA/profile")

"""
Nous avons utilisé le package requests pour obtenir les données et les transmettre à la fonction read_html().
Un en-tête de requête est utilisé dans une requête HTTP pour fournir des informations sur le contexte de la requête, afin que le serveur puisse personnaliser la réponse. Nous avons fourni des données pour un navigateur Web standard.
"""

url_link = "https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA"
data = pd.read_html(r.text)
print(data[0])
print()

data = data[data["Earnings Estimate"] == "Avg.Estimate"]
data.plot(kind="bar")

url_link = "https://www.test.com"
data = pd.read_html(url_link)
print(data[2])
print()