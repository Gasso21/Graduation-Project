from module import BusNo2BusId, BusId2Coordi, Coordi2Place
import pandas as pd

# Input
bus_number = input("버스번호를 입력하시오: ")

# Bus Number -> Bus ID
busRouteId = BusNo2BusId.getBusRouteList(bus_number)

# Bus ID -> Coordinates List
gpsList = BusId2Coordi.getStationByRoute(busRouteId)

# Coordinates List -> Places(-gu)
placeList = []
for lon, lat in gpsList:
    placeList.append(Coordi2Place.reversegeocoding(lat, lon))

# Deduplicate Places(-gu)
placeList = list(set(placeList))
#place_str = ','.join(s for s in placeList)
place_str = ','.join(map(str, placeList))

df = pd.read_csv('./module/Crawling.csv')
place_time = df['Update Time'][0].replace('(','')
place_time = place_time.replace(')','')

total_people, today_people = 0,0
for i in placeList:
    total_people += int(df[i][0].replace(',',''))
    today_people += int(df[i][1].replace(',',''))

#total_people = format(total_people, ',d')
#today_people = format(today_people, ',d')

print(df)
print('{0}번 버스가 지나는 자치구는 {1}입니다.' .format(bus_number,place_str))
print('현재 코로나 업데이트는 {0}이며,' .format(place_time))
print('해당 자치구의 \t누적 확진자수는 {0:,}명,\n \t\t신규 확진자수는 {1:,}명입니다.' .format(total_people, today_people))