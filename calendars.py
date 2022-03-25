from bs4 import BeautifulSoup
import requests
import requests_cache
requests_cache.install_cache('foot_cache')

url = r'https://fbref.com/fr/equipes/361ca564/Statistiques-Tottenham-Hotspur'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

div = soup.find('div', {'id': 'all_matchlogs'})

title = div.find('h2').get_text()
table = div.find('table')

data_calendar = []

calendars = {}

data_calendar.append(title)

for rows in table.findAll('tr'):
    date = rows.findAll('th')
    infos = rows.findAll('td')
    if len(infos) > 0:
        calendars = { 
            "calendar" : 
            {
                "info": {
                    'date': date[0].text.strip(),
                    'heure': infos[0].text.strip(),
                    'comp': infos[1].text.strip(),
                    'Tour': infos[2].text.strip(),
                    'Jour': infos[3].text.strip(),
                    'Tribune': infos[4].text.strip(),
                    'Résultat': infos[5].text.strip(),
                    'BM': infos[6].text.strip(),
                    'BE': infos[7].text.strip(),
                    'Adversaire': infos[8].text.strip(),
                    'xG': infos[9].text.strip(),
                    'xGA': infos[10].text.strip(),
                    'Poss': infos[11].text.strip(),
                    'Affluence': infos[12].text.strip(),
                    'Capitaine': infos[13].text.strip(),
                    'Formation': infos[14].text.strip(),
                    'Arbitre': infos[15].text.strip(),
                    'Rapport': infos[16].text.strip(),
                },
            },
        }
        data_calendar.append(calendars)

print(data_calendar)