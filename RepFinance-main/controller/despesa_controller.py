from controller.decorators import handle_exceptions_and_logging
from persistence.despesa_dao import DespesaDAO  # Importando o DAO
from model.despesa_model import DespesaModel

class DespesaController:
    def __init__(self):
        self.despesa_dao = DespesaDAO()

    @handle_exceptions_and_logging
    def get_despesas(self):
        """Retorna todas as despesas cadastradas."""
        return self.despesa_dao.get_all()

    @handle_exceptions_and_logging
    def cadastrar_despesa(self, descricao, usuario, valor, mes_vencimento, ano_vencimento, categoria=""):
        """Cadastra uma nova despesa e retorna a lista atualizada de despesas."""
        # Cadastra a nova despesa
        self.despesa_dao.create(descricao, usuario, float(valor), int(mes_vencimento), int(ano_vencimento), categoria)
        # Retorna a lista completa de despesas após o cadastro
        return self.get_despesas()

    @handle_exceptions_and_logging
    def apagar_despesa(self, codigo):
        """Apaga uma despesa e retorna a lista atualizada de despesas."""
        self.despesa_dao.delete(codigo)
        return self.get_despesas()

    @handle_exceptions_and_logging
    def buscar_por_descricao(self, descricao_buscar):
        """Busca despesas por descrição e retorna a lista correspondente."""
        despesas = self.get_despesas()
        return [despesa for despesa in despesas if descricao_buscar.lower() in despesa.descricao.lower()]
