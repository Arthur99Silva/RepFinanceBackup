from controller.decorators import handle_exceptions_and_logging
from persistence.compra_dao import CompraDAO  # Importando o DAO

class CompraController:
    def __init__(self):
        self.compra_dao = CompraDAO()

    @handle_exceptions_and_logging
    def get_compras(self):
        return self.compra_dao.get_all()

    @handle_exceptions_and_logging
    def cadastrar_compra(self, descricao, usuario, valor):
        # Cadastra a compra e depois retorna todas as compras
        self.compra_dao.create(descricao, usuario, valor)
        return self.get_compras()  # Retorna uma lista de todas as compras

    @handle_exceptions_and_logging
    def apagar_compra(self, codigo):
        self.compra_dao.delete(codigo)
        return self.get_compras()  # Retorna uma lista atualizada de compras

    @handle_exceptions_and_logging
    def buscar_por_descricao(self, descricao_buscar):
        compras = self.get_compras()
        return [compra for compra in compras if descricao_buscar.lower() in compra.descricao.lower()]
