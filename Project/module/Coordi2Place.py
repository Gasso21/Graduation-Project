def reversegeocoding(lat, lon):
    from urllib.parse import urlencode
    import requests

    # API URL & Key
    T_url = "https://apis.openapi.sk.com/tmap/geo/reversegeocoding"
    appKey = 'l7xxc36f3069b6d149139927d7bfae4e9312'

    # Parameters
    params = {}
    params['version'] = '1'
    params['lat'] = lat
    params['lon'] = lon
    params['coordType'] = 'WGS84GEO'
    params['addressType'] = 'A00'
    params['appKey'] = appKey

    # Request
    queryParams = '?' + urlencode(params)
    resp = requests.get(T_url + queryParams)

    # Parsing
    response_body = resp.json()

    # Select text and make list
    gu = response_body["addressInfo"]["gu_gun"]
    return gu


if __name__ == "__main__":
    gu_name = reversegeocoding(37.5050881, 126.9571012)
    print("Address(-gu) name: ", gu_name)