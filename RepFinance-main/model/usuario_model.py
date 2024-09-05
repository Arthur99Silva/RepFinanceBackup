from kivy.properties import StringProperty


class UsuarioModel:

    def __init__(
        self, cod="0", usuario="", senha="", nome="", saldo=0, role=["morador"]
    ) -> None:
        self._cod = cod
        self._usuario = usuario
        self._senha = senha
        self._nome = nome
        self._saldo = saldo
        self._role = role

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod):
        self._cod = cod

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role
