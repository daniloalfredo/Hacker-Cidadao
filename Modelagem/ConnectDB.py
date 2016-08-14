import MySQLdb

class connectMysql:
    def __init__(self, url, user, password, bd):
        self.db = MySQLdb.connect(url, user, password, bd)
        self.cursor = self.db.cursor()

    def closeConnect(self):
        self.db.close();

    def getConnect(self):
        return self.db
