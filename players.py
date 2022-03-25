from bs4 import BeautifulSoup
import requests
import requests_cache
requests_cache.install_cache('foot_cache')

url = r'https://fbref.com/fr/equipes/361ca564/Statistiques-Tottenham-Hotspur'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

div = soup.find('div', {'id': 'all_stats_standard'})

title = div.find('h2').get_text()
table = div.find('table')

data_stats = []

joueurs = {}

data_stats.append(title)

for rows in table.findAll('tr'):
    name = rows.findAll('th')
    infos = rows.findAll('td')
    if len(infos) > 0:
        joueurs = { 
            "joueur" : 
            {
                "info": {
                    'Name': name[0].text.strip(),
                    'Nation': infos[0].text.strip(),
                    'Position': infos[1].text.strip(),
                    'Age': infos[2].text.strip(),
                },
                "Temps de jeu": {
                    'MJ': infos[3].text.strip(),
                    'Titulaire': infos[4].text.strip(),
                    'Min': infos[5].text.strip(),
                    '90': infos[6].text.strip(),
                },
                "Performance": {
                    'But': infos[7].text.strip(),
                    'PD': infos[8].text.strip(),
                    'B-PénM': infos[9].text.strip(),
                    'PénM': infos[10].text.strip(),
                    'PénT': infos[11].text.strip(),
                    'CJ': infos[12].text.strip(),
                    'CR': infos[13].text.strip(),
                },
                "Par 90 minutes (1)": {
                    'Buts': infos[14].text.strip(),
                    'PD': infos[15].text.strip(),
                    'B+PD': infos[16].text.strip(),
                    'B-Pénm': infos[17].text.strip(),
                    'B+PD-PénM': infos[18].text.strip(),
                },
                "Attendu": {
                    'xG': infos[19].text.strip(),
                    'npxG': infos[20].text.strip(),
                    'xA': infos[21].text.strip(),
                    'npxG+xA': infos[22].text.strip(),
                },
                "Par 90 minutes (2)": {
                    'xG': infos[23].text.strip(),
                    'xA': infos[24].text.strip(),
                    'xG+xA': infos[25].text.strip(),
                    'npxG': infos[26].text.strip(),
                    'npxG+xA': infos[27].text.strip(),
                },
                "Matchs": infos[28].text.strip(),
            },
        }
        data_stats.append(joueurs)

print(data_stats)