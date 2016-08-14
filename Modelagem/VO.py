class CidadeVO:
	def __init__(self):
		self.id = None
		self.name = None

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setId(self, idCidade):
		self.id = idCidade

	def setName(self, NameCity):
		self.name = NameCity

class LocalVO:
	def __init__(self):
		self.id = None
		self.name = None
		self.address = None
		self.tipo = None
		self.area = None
		self.perimeter = None
		self.codbairro = None
		self.nomebairro = None
		self.clogra = None
		self.idCidade = None

	def getId(self):
		return self.id

	def setId(self, idLocal):
		self.id = idLocal

	def getName(self):
		return self.name

	def setName(self, nameLocal):
		self.name = nameLocal

	def getAddress(self):
		return self.address

	def setAddress(self, Address):
		self.address = Address

	def getTipo(self):
		return self.tipo

	def setTipo(self, Tipo):
		self.tipo = Tipo

	def getArea(self):
		return self.area

	def setArea(self, Area):
		self.area = Area 

	def getPerimeter(self):
		return self.perimeter

	def setPerimeter(self, Perimeter):
		self.perimeter = Perimeter

	def getCodBairro(self):
		return self.codbairro

	def setCodBairro(self, CodBairro):
		self.codbairro = CodBairro

	def getNomeBairro(self):
		return self.nomebairro

	def setNomeBairro(self, NomeBairro):
		self.nomebairro = NomeBairro

	def getClogra(self):
		return self.clogra

	def setClogra(self, Clogra):
		self.clogra = Clogra 

	def getIdCidade(self):
		return self.idCidade

	def setIdCidade(self, idCidade):
		self.idCidade = idCidade

class AgendaVO:
	def __init__(self):
		self.id = None
		self.name = None
		self.dia = None
		self.horaBegin = None
		self.horaEnd = None
		self.idLocal = None

	def getId(self):
		return self.id

	def setId(self, idAgenda):
		self.id = idAgenda

	def getName(self):
		return self.name

	def setName(self, Name):
		self.name = Name

	def getDia(self):
		return self.dia

	def setDia(self, Dia):
		self.dia = Dia

	def getHoraBegin(self):
		return self.horaBegin

	def setHoraBegin(self, HoraBegin):
		self.horaBegin = HoraBegin

	def getHoraEnd(self):
		return self.horaEnd

	def setHoraEnd(self, HoraEnd):
		self.horaEnd = HoraEnd

	def getIdLocal(self):
		return self.idLocal

	def setIdLocal(self, IdLocal):
		self.idLocal = IdLocal

class SensorVO:
	def __init__(self):
		self.id = None
		self.name = None
		self.tipo = None
		self.unidade = None
		self.valor = None
		self.IdLocal = None

	def getId(self):
		return self.id

	def setId(self, idSensor):
		self.id = idSensor

	def getName(self):
		return self.name

	def setName(self, Name):
		self.name = Name

	def getTipo(self):
		return self.tipo

	def setTipo(self, Tipo):
		self.tipo = Tipo

	def getUnidade(self):
		return self.unidade

	def setUnidade(self, Unidade):
		self.unidade = Unidade

	def getValor(self):
		return self.valor

	def setValor(self, Valor):
		self.valor = Valor

	def getIdLocal(self):
		return self.idLocal

	def setIdLocal(self, IdLocal):
		self.idLocal = IdLocal

class RelatorioVO:
	def __init__(self):
		self.id = None
		self.descricao = None
		self.categ = None
		self.idLocal = None

	def getId(self):
		return self.id

	def setId(self, idRelatorio):
		self.id = idRelatorio

	def getDescricao(self):
		return self.descricao

	def setDescricao(self, Descricao):
		self.descricao = Descricao

	def getCateg(self):
		return self.categ

	def setCateg(self, Categ):
		self.categ = Categ

	def getIdLocal(self):
		return self.idLocal

	def setIdLocal(self, IdLocal):
		self.idLocal = IdLocal

class UserVO:
	def __init__(self):
		self.id = None
		self.name = None
		self.login = None
		self.password = None

	def getId(self):
		return self.id

	def setId(self, idUser):
		self.id = idUser

	def getName(self):
		return self.name

	def setName(self, Name):
		self.name = Name

	def getLogin(self):
		return self.login

	def setLogin(self, Login):
		self.login = Login

	def getPassword(self):
		return self.password

	def setPassword(self, Password):
		self.password = Password