from controller.decorators import handle_exceptions_and_logging
from persistence.usuario_dao import UsuarioDAO  # Importando o DAO

class UsuarioController:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()  # Inicializando o DAO

    @handle_exceptions_and_logging
    def login(self, usuario, senha):
        usuario_data = self.usuario_dao.get_by_usuario(usuario)
        if usuario_data and usuario_data.senha == senha:
            return usuario_data
        return None

    @handle_exceptions_and_logging
    def get_usuarios(self):
        return self.usuario_dao.get_all()

    @handle_exceptions_and_logging
    def cadastrar_usuario(self, nome, usuario, senha, saldo):
        novo_usuario = {
            "cod": str(int(self.usuario_dao.get_all()[-1].cod) + 1),  # Gerando um novo ID
            "usuario": usuario,
            "senha": senha,
            "nome": nome,
            "saldo": saldo,
            "role": "user",  # Default role
        }
        return self.usuario_dao.create(**novo_usuario)

    @handle_exceptions_and_logging
    def apagar_usuario(self, cod):
        return self.usuario_dao.delete(cod)

    @handle_exceptions_and_logging
    def buscar_por_nome(self, nome_buscar):
        # Supondo que o DAO tenha um método similar para busca por nome
        usuarios = self.usuario_dao.get_all()
        return [usuario for usuario in usuarios if nome_buscar.lower() in usuario.nome.lower()]
