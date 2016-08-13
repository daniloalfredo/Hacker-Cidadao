import json
from urllib import urlopen
from pprint import pprint
#url = "http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php"

def getTempData(url):
    jsondata = urlopen(url)
    data = json.loads(jsondata.read())
    temperatura = data["Sensor"][15]["Valor"]
    #print temperatura
    return temperatura
