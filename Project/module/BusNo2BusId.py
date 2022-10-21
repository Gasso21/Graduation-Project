def getBusRouteList(strSrch):
    from urllib.parse import urlencode, unquote
    from urllib.request import Request, urlopen
    import xml.etree.ElementTree as ET
    
    #API URL & Key
    url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList'
    ServiceKey = unquote('gjPavFovnjVJ7CFP7V%2FeNq3fwMNiW4GVn%2FNDcWSTJpqb1uII9BrKZJ8Vq2vZmYbm3ahPDMhFY7pF5e7jcfwy7w%3D%3D')

    #Parameters
    params = {}
    params['ServiceKey'] = ServiceKey
    params['strSrch'] = strSrch
    
    #Request
    queryParams = '?' + urlencode(params)
    request = Request(url + queryParams)
    #request.get_method = lambda: 'GET'

    #parsing
    doc = ET.parse(urlopen(request))
    
    root = doc.getroot()
    msgBody    = root.find("msgBody")
    itemList   = msgBody.find("itemList")
    busRouteId = itemList.find("busRouteId").text

    return busRouteId

if __name__ == "__main__":
    bus_number = input("버스 번호를 입력하시오: \n")
    bus_Id = getBusRouteList(bus_number)
    print("Bus Route ID : ",bus_Id)