from Sensor import getEmbarqueLab
from Sensor import getParquesPracas
from flask import Flask, request, render_template, url_for
from geojson import Feature, Point
from geojson import FeatureCollection
import json
import geojson

from flask import Flask, request, render_template, url_for



##################DADOS SENSORES##########################
# 6 - temp 7 - umidade 9 - luminosidade 17 - Pressao do ar


#for x in listaSensores:
#	print x[0]
#	print x[1]
#	print x[2]
#	print "'''"


###################DADOS PARQUES PRACAS#################
# 498 = Quantidade de pracas ou parques no json
#x = getParquesPracas(498)
#x = getParquesPracas(498)
#x = getParquesPracas(1)



#for i in range(0,498):
#	print x[i]
## retorno.append([nome,ed,tipo,area,perimetro,bairroCode,nomeBairro,lograCode, sensores])

## [0] = nome
## [1] = ed (indereco)
## [2] = tipo
## [3] = area
## [4] = perimetro
## [5] = codigo bairro
## [6] = nome bairro
## [7] = logradouro
## [8] = sensores (temperatura, umidade, luminosidade ,pressao)
## [9] = geometry

###################DADOS PARQUES PRACAS#################

'''for i in x:
	my_feature = geojson.Feature(properties={"Nome do Local": i[0], "Endereco": i[1], "Tipo de Area": i[2],
		"Area": i[3], "Perimetros": i[4], "Codigo do Bairro": i[5], "Nome do Bairro": i[6], 
		"Logradouro": i[7], "Sensor de Temperatura": i[8][0][0], "Sensor de Umidade": i[8][1],
		"Sensor de Luminosidade": i[8][2], "Sensor de Pressao" : i[8][3], "Eventos" : ""
		},geometries={"coordinates":i[9]})
	my_other_feature =  geojson.Feature(my_feature)
	print FeatureCollection(my_other_feature)
'''
'''jsonFile = ""
for i in x:
	dictionary = {"Nome do Local": i[0], "Endereco": i[1], "Tipo de Area": i[2],
		"Area": i[3], "Perimetros": i[4], "Codigo do Bairro": i[5], "Nome do Bairro": i[6], 
		"Logradouro": i[7], "Sensor de Temperatura": i[8][0], "Sensor de Umidade": i[8][1],
		"Sensor de Luminosidade": i[8][2], "Sensor de Pressao" : i[8][3], "Eventos" : ""}
	jsonFile += json.dumps(dictionary)

print jsonFile '''


app = Flask(__name__)

@app.route('/')
def choice():
	return render_template('index.html')

@app.route('/mapa')
def renderT():
	return render_template('event.html')

if __name__ == '__main__':
	from tornado.wsgi import WSGIContainer
	from tornado.httpserver import HTTPServer
	from tornado.ioloop import IOLoop

	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5000);
	IOLoop.instance().start()

#print my_feature
##foo12.geojson
#
#>>> my_feature = Feature(geometry=Point((1.6432, -19.123)))
#
#>>> my_other_feature = Feature(geometry=Point((-80.234, -22.532)))
#
#>>> FeatureCollection([my_feature, my_other_feature])  # doctest: +ELLIPSIS
#{"features": [{"geometry": {"coordinates": [1.643..., -19.12...], "type": "Point"}