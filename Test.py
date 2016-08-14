import MySQLdb
from Modelagem.VO import CidadeVO 

cidade = CidadeVO()
cidade.setName("Hellcife")
conn = MySQLdb.connect("localhost", "cidade", "senha", "hackercidadao")
query = "SELECT * FROM Cidade"
cursor = conn.cursor()
cursor.execute(query)
#result = cursor.fetchall()
conn.commit()
conn.close()
for row in cursor:
	print(row) 