from Sensor import getEmbarqueLab
from flask import Flask, request, render_template, url_for
import json

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