import FactoryConnect 
import md5
import datetime
from VO import CidadeVO, LocalVO, AgendaVO, SensorVO, RelatorioVO, UserVO

class CidadeDAO:
	def __init__(self):
		self.con = FactoryConnect.FactoryBD()

	def insert(self, City):
		try:
			query = "INSERT INTO `Cidade`(`Name`) VALUES('" + str(City.getName()) + "')"
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao inserir Cidade"
			return False

	def delete(self, idCidade):
		try:
			query = "DELETE FROM Cidade where id=" + str(idCidade)
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao deletar Cidade"
			return False

	def getListAll(self):
		try:
			query = "SELECT * FROM Cidade"
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return result
		except Exception as e:
			print "Erro ao listar cidades"
			return False

	def getList(self, consulta):
		try:
			query = "SELECT * FROM Cidade where" + str(consulta)
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			retorno = CidadeVO()
			for row in result:
				retorno.setId(row[0])
				retorno.setName(row[1])
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return retorno
		except Exception as e:
			print "Erro ao listar cidades"
			return False

class LocalDAO:
	def __init__(self):
		self.con = FactoryConnect.FactoryBD()

	def insert(self, Local):
		try:
			query = "INSERT INTO `Local`(`Name`, `Address`, `Tipo`, `Area`, `Perimeter`, `CodBairro`, `NomeBairro`, `Clogra`, `Id_City`) VALUES('" + str(Local.getName()) + "', '" + str(Local.getAddress()) + "', '"+ str(Local.getTipo()) "', '" +str(Local.getArea())"', '"+ str(Local.getPerimeter())"', '"+ str(Local.getCodBairro()"', '" + str(Local.getNomeBairro()"', '"+ str(Local.getClogra()"', '"+str(Local.getIdCidade()"');"
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao inserir Local"
			return False

	def delete(self, idLocal):
		try:
			query = "DELETE FROM Local where id=" + str(idLocal)
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao deletar Local"
			return False

	def getListAll(self):
		try:
			query = "SELECT * FROM Local"
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return result
		except Exception as e:
			print "Erro ao listar Locals"
			return False

	def getList(self, consulta):
		try:
			query = "SELECT * FROM Local where" + str(consulta)
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			retorno = LocalVO()
			for row in result:
				retorno.setId(row[0])
				retorno.setName(row[1])
				retorno.setAddress(row[2])
				retorno.setTipo(row[3])
				retorno.setArea(row[4])
				retorno.setPerimeter(row[5])
				retorno.setCodBairro(row[6])
				retorno.setNomeBairro(row[7])
				retorno.setClogra(row[8])
				retorno.setIdCidade(row[9])
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return retorno
		except Exception as e:
			print "Erro ao listar cidades"
			return False

class AgendaDAO:
	def __init__(self):
		self.con = FactoryConnect.FactoryBD()

	def insert(self, Agenda):
		try:
			query = "INSERT INTO `Agenda` (`Name`, `Dia`, `HoraBegin`, `HoraEnd`, `Id_Local`) VALUES ('"+ str(Agenda.getName())"', '"+ str(Agenda.getDia())"', '"+ str(Agenda.getHoraBegin())"', '"+ str(Agenda.getHoraEnd())"', '"+ str(Agenda.getIdLocal())"');"
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao inserir Agenda"
			return False

	def delete(self, idAgenda):
		try:
			query = "DELETE FROM Agenda where id=" + str(idAgenda)
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao deletar Agenda"
			return False

	def getListAll(self):
		try:
			query = "SELECT * FROM Agenda"
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return result
		except Exception as e:
			print "Erro ao listar Agendas"
			return False

	def getList(self, consulta):
		try:
			query = "SELECT * FROM Agenda where" + str(consulta)
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			retorno = AgendaVO()
			for row in result:
				retorno.setId(row[0])
				retorno.setName(row[1])
				retorno.setDia(row[2])
				retorno.setHoraBegin(row[3])
				retorno.setHoraEnd(row[4])
				retorno.setIdLocal(row[5])
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return retorno
		except Exception as e:
			print "Erro ao listar Agenda"
			return False

class SensorDAO:
	def __init__(self):
		self.con = FactoryConnect.FactoryBD()

	def insert(self, Sensor):
		try:
			query = "INSERT INTO `Sensor` (`Name`, `Tipo`, `Unidade`, `Valor`, `Id_Local`) VALUES ('"+ str(Sensor.getName())"', '"+ str(Sensor.getTipo())"', '"+ str(Sensor.getUnidade())"', '"+ str(Sensor.getValor())"', '"+ str(Sensor.getIdLocal())"');"
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao inserir Sensor"
			return False

	def delete(self, idSensor):
		try:
			query = "DELETE FROM Sensor where id=" + str(idSensor)
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao deletar Sensor"
			return False

	def getListAll(self):
		try:
			query = "SELECT * FROM Sensor"
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return result
		except Exception as e:
			print "Erro ao listar Sensors"
			return False

	def getList(self, consulta):
		try:
			query = "SELECT * FROM Sensor where" + str(consulta)
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			retorno = SensorVO()
			for row in result:
				retorno.setId(row[0])
				retorno.setName(row[1])
				retorno.setTipo(row[2])
				retorno.setUnidade(row[3])
				retorno.setValor(row[4])
				retorno.setIdLocal(row[5])
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return retorno
		except Exception as e:
			print "Erro ao listar Sensor"
			return False

class RelatorioDAO:
	def __init__(self):
		self.con = FactoryConnect.FactoryBD()

	def insert(self, Relatorio):
		try:
			query = "INSERT INTO `Relatorio` (`Descricao`, `Categ`, `Id_Local`) VALUES ('"+ str(Relatorio.getDescricao())"', '"+ str(Relatorio.getCateg())"', '"+ str(Relatorio.getIdLocal())"');"
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao inserir Relatorio"
			return False

	def delete(self, idRelatorio):
		try:
			query = "DELETE FROM Relatorio where id=" + str(idRelatorio)
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao deletar Relatorio"
			return False

	def getListAll(self):
		try:
			query = "SELECT * FROM Relatorio"
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return result
		except Exception as e:
			print "Erro ao listar Relatorios"
			return False

	def getList(self, consulta):
		try:
			query = "SELECT * FROM Relatorio where" + str(consulta)
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			retorno = RelatorioVO()
			for row in result:
				retorno.setId(row[0])
				retorno.setDescricao(row[1])
				retorno.setCateg(row[2])
				retorno.setIdLocal(row[3])
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return retorno
		except Exception as e:
			print "Erro ao listar Relatorio"
			return False

class UserDAO:
	def __init__(self):
		self.con = FactoryConnect.FactoryBD()

	def insert(self, User):
		try:
			query = "INSERT INTO `User` (`Name`, `login`, `password`) VALUES ('"+ str(User.getName())"', '"+ str(User.getLogin())"', '"+ str(User.getPassword())"');"
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao inserir User"
			return False

	def delete(self, idUser):
		try:
			query = "DELETE FROM User where id=" + str(idUser)
			self.con.conn.cursor.execute(query)
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return True
		except Exception as e:
			print "Erro ao deletar User"
			return False

	def getListAll(self):
		try:
			query = "SELECT * FROM User"
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return result
		except Exception as e:
			print "Erro ao listar Users"
			return False

	def getList(self, consulta):
		try:
			query = "SELECT * FROM User where" + str(consulta)
			self.con.conn.cursor.execute(query)
			result = self.con.conn.cursor.fetchall()
			retorno = UserVO()
			for row in result:
				retorno.setId(row[0])
				retorno.setName(row[1])
				retorno.setLogin(row[2])
				retorno.setLogin(row[3])
			self.con.conn.db.commit()
			self.con.conn.closeConnect()
			return retorno
		except Exception as e:
			print "Erro ao listar User"
			return False