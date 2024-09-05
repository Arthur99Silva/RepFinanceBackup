from datetime import date


class CompraModel:

    def __init__(
        self,
        codigo="",
        descricao="",
        status="pendente",
        usuario="",
        valor=0,
        mes=date.today().month,
        ano=date.today().year,
    ):
        self._codigo = codigo
        self._descricao = descricao
        self._status = status
        self._usuario = usuario
        self._valor = valor
        self._mes = mes
        self._ano = ano

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, mes):
        self._mes = mes

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano
