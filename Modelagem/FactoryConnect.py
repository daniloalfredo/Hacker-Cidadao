import ConnectDB

class FactoryBD:
	def __init__(self):
		self.conn = ConnectDB.connectMysql("localhost", "cidade", "senha", "hackercidadao");