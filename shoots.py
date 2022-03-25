from bs4 import BeautifulSoup
import requests
import requests_cache
requests_cache.install_cache('foot_cache')

url = r'https://fbref.com/fr/equipes/361ca564/Statistiques-Tottenham-Hotspur'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

div = soup.find('div', {'id': 'all_stats_shooting'})

title = div.find('h2').get_text()
table = div.find('table')

data_shoots = []

shoots = {}

data_shoots.append(title)

for rows in table.findAll('tr'):
    player = rows.findAll('th')
    infos = rows.findAll('td')
    if len(infos) > 0:
        shoots = { 
            "shoot" : 
            {
                "Joueur": player[0].text.strip(),
                "Nation": infos[0].text.strip(),
                "Pos": infos[1].text.strip(),
                "Age": infos[2].text.strip(),
                "90": infos[3].text.strip(),
                "Standard": {
                    'Buts': infos[4].text.strip(),
                    'Tirs': infos[5].text.strip(),
                    'TC': infos[6].text.strip(),
                    'TC %': infos[7].text.strip(),
                    'Tir/90': infos[8].text.strip(),
                    'TC/90': infos[9].text.strip(),
                    'B/Tir': infos[10].text.strip(),
                    'B/TC': infos[11].text.strip(),
                    'Dist': infos[12].text.strip(),
                    'CF': infos[13].text.strip(),
                    'PénM': infos[14].text.strip(),
                    'PénT': infos[15].text.strip(),
                },
                "Attendu": {
                    "xG": infos[16].text.strip(),
                    "npxG": infos[17].text.strip(),
                    "npxG/Sh": infos[18].text.strip(),
                    "G-xG": infos[19].text.strip(),
                    "np:G-xG": infos[20].text.strip(),
                },
                "Match": infos[21].text.strip(),
            },
        }
        data_shoots.append(shoots)

print(data_shoots)