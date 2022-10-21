import pandas as pd
import requests, bs4

response = requests.get('https://www.seoul.go.kr/coronaV/coronaStatus.do')
html_obj = bs4.BeautifulSoup(response.content, 'html.parser')

ths = html_obj.select('table.tstyle-status.pc.pc-table > tbody > tr > th')
tds_total = html_obj.select('table.tstyle-status.pc.pc-table > tbody > tr > td:not(.today)')
tds_today = html_obj.select('table.tstyle-status.pc.pc-table > tbody > tr > td.today')
place_time = html_obj.select(' div#wrap.sub > div#container > div.layout-inner.layout-sub > div.inner.inner7 > div#move-cont1.move-cont > p.update-date')

data = {}    
for i in range(len(ths)):
    data[ths[i].text] = [tds_total[i].text, tds_today[i].text]

Crawling = pd.DataFrame(data, index=['Total', 'Today'])
Crawling.loc['Total','Update Time'] = place_time[0].text

Crawling.to_csv('Crawling.csv', encoding='utf-8-sig')