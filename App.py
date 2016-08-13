from Sensor import getTempData
urlSensor = "http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php"

print getTempData(urlSensor)
