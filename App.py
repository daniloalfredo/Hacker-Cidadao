from Sensor import getTempData
from flask import Flask, request, render_template, url_for
import json
urlSensor = "http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php"

print getTempData(urlSensor)
