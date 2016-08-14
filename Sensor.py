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

def getParquesPracas(j):
	urlSensor = "http://dados.recife.pe.gov.br/storage/f/2014-05-23T19%3A41%3A50.416Z/parquespracas.geojson"
	jsondata = urlopen(urlSensor)
	data = json.loads(jsondata.read())

	#print ch.encode('ascii', 'ignore')
	retorno = []

	for i in range(0,j):
		nome = data["features"][i]["properties"]["NMNOME"]
		nome = (unicode(nome).encode('utf8'))
	
		ed = data["features"][i]["properties"]["ED"]
		ed = (unicode(ed).encode('utf8'))
		
		tipo = data["features"][i]["properties"]["CDTIPO"]
		tipo = (unicode(tipo).encode('utf8'))
		
		area = data["features"][i]["properties"]["AREA"]
		area = (unicode(area).encode('utf-8'))
		
		perimetro = data["features"][i]["properties"]["PERIMETER"]
		perimetro = (unicode(perimetro).encode('utf-8'))
		
		bairroCode = data["features"][i]["properties"]["CBAIRRCODI"]
	 	bairroCode = (unicode(bairroCode).encode('utf-8'))
		
		nomeBairro = data["features"][i]["properties"]["NOMEBAIRR"]
		nomeBairro = (unicode(nomeBairro).encode('utf-8'))
		
		lograCode = data["features"][i]["properties"]["CLOGRACOD"]
		lograCode =  (unicode(lograCode).encode('utf-8'))

		retorno.append([nome,ed,tipo,area,perimetro,bairroCode,nomeBairro,lograCode])

	return retorno

