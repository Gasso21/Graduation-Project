def getStationByRoute(busRouteId):
    from urllib.parse import urlencode, unquote
    from urllib.request import Request, urlopen
    import xml.etree.ElementTree as ET

    # API URL & Key
    url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute'
    ServiceKey = unquote('gjPavFovnjVJ7CFP7V%2FeNq3fwMNiW4GVn%2FNDcWSTJpqb1uII9BrKZJ8Vq2vZmYbm3ahPDMhFY7pF5e7jcfwy7w%3D%3D')

    # Parameters
    params = {}
    params['ServiceKey'] = ServiceKey
    params['busRouteId'] = busRouteId

    # Request
    queryParams = '?' + urlencode(params)
    request = Request(url + queryParams)

    # Parsing
    with urlopen(request) as response:
        res_xml = ET.parse(response)

    # Select text and make list
    root = res_xml.getroot()
    msgBody = root.find("msgBody")
    gpsList = list()

    for itemList in msgBody.findall("itemList"):
        gpsX = itemList.find("gpsX").text
        gpsY = itemList.find("gpsY").text
        gps = [gpsX, gpsY]
        gpsList.append(gps)
    return gpsList


if __name__ == "__main__":
    Coordi = getStationByRoute(100100081)
    print("========Bus Station's GPS Address======== ")
    for i in Coordi:
        print(i)