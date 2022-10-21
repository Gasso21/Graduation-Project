import pandas as pd
import requests, bs4

response = requests.get('https://www.seoul.go.kr/coronaV/coronaStatus.do')
html_obj = bs4.BeautifulSoup(response.content, 'html.parser')

ths = html_obj.select('table.tstyle-status.pc.pc-table > tbody > tr > th')
tds = html_obj.select('table.tstyle-status.pc.pc-table > tbody > tr > td')
place_time = html_obj.select(' div#wrap.sub > div#container > div.layout-inner.layout-sub > div.inner.inner7 > div#move-cont1.move-cont > p.update-date')

name_list = []
total_value = []
today_value = []

for i in range(0, len(ths)):
    #자치구 이름
    columns = ths[i].text
    #print(columns)
    name_list.append(columns)
    
for i in range(0, len(tds)):
    rows = tds[i].text
    if (i//(len(ths)/2))%2 == 0:
        total_value.append(rows)
    else:
        today_value.append(rows)

Crawling = pd.DataFrame([total_value,today_value], columns=name_list, index=['Total', 'Today'])
Crawling.loc['Total','Update Time'] = place_time[0].text

Crawling.to_csv('Crawling.csv', encoding='utf-8-sig')