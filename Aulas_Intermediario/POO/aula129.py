# revendo e praticando a diferença entre method - @classmethod e @staticmethod


class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_user(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def somar_parcelas(a, b):
        return a + b

    @staticmethod
    def connection_log(msg):
        print(f"Enviando log: {msg}")


c1 = Connection.create_with_user("jao", "123456")

# c1 = Connection()
# c1.set_user("jao")
# c1.set_password("123456")
print(Connection.somar_parcelas(1, 2))
print(c1.user)
print(c1.password)
Connection.connection_log("Log de teste")
