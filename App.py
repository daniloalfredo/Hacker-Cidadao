from Sensor import getEmbarqueLab
from Sensor import getParquesPracas
from flask import Flask, request, render_template, url_for
import json


##################DADOS SENSORES##########################
# 6 - temp 7 - umidade 9 - luminosidade 17 - Pressao do ar
listaSensores = []
sensorAcesso = [6,7,9,17]

for x in sensorAcesso:
	retorno =  getEmbarqueLab(x)
	listaSensores.append(retorno)

#for x in listaSensores:
#	print x[0]
#	print x[1]
#	print x[2]
#	print "'''"


###################DADOS PARQUES PRACAS#################
# 498 = Quantidade de pracas ou parques no json
x = getParquesPracas(498)

#for i in range(0,498):
#	print x[i]

###################DADOS PARQUES PRACAS#################
