from datetime import date

class DespesaModel:
    def __init__(
        self,
        codigo="",
        descricao="",
        status="pendente",
        usuario="",
        valor=0,
        mes_vencimento=0,
        ano_vencimento=0,
        mes=date.today().month,
        ano=date.today().year,
        categoria=""
    ):
        self._codigo = codigo
        self._descricao = descricao
        self._status = status
        self._usuario = usuario
        self._valor = valor
        self._mes_vencimento = mes_vencimento
        self._ano_vencimento = ano_vencimento
        self._mes = mes
        self._ano = ano
        self._categoria = categoria

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
    def mes_vencimento(self):
        return self._mes_vencimento

    @mes_vencimento.setter
    def mes_vencimento(self, mes_vencimento):
        self._mes_vencimento = mes_vencimento

    @property
    def ano_vencimento(self):
        return self._ano_vencimento

    @ano_vencimento.setter
    def ano_vencimento(self, ano_vencimento):
        self._ano_vencimento = ano_vencimento

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

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
