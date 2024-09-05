class CompraModel:

    def __init__(self, codigo, descricao, status) -> None:
        self._codigo = codigo
        self._descricao = descricao
        self._status = status

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
