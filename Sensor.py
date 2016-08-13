import json
from urllib import urlopen
from pprint import pprint
#url = "http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php"

def getEmbarqueLab(i):
	urlSensor = "http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php"
	jsondata = urlopen(urlSensor)
	data = json.loads(jsondata.read())
	nome = data["Sensor"][i-1]["Nome"]
	descricao = data["Sensor"][i-1]["Descricao"]
	valor = data["Sensor"][i-1]["Valor"]
	return nome, descricao, valor