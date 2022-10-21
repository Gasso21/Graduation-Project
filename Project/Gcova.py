from urllib.parse import urlencode, unquote
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from module import BusNo2BusId
busRouteId = BusNo2BusId.getBusRouteList(506)
print(busRouteId)