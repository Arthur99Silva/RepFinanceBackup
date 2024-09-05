import json
from persistence.base_dao import BaseDAO
from model.usuario_model import UsuarioModel

class UsuarioDAO(BaseDAO):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UsuarioDAO, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'file_path'):
            self.file_path = "data/Usuario.json"

    def get_all(self):
        """Retorna todos os usuários."""
        with open(self.file_path, "r") as usuarios_json:
            usuarios = json.load(usuarios_json)
        return [
            UsuarioModel(
                cod=u["cod"],
                usuario=u["usuario"],
                senha=u["senha"],
                nome=u["nome"],
                saldo=u["saldo"],
                role=u["role"],
            )
            for u in usuarios["usuarios"]
        ]

    def get_by_id(self, usuario_id):
        """Busca um usuário por ID."""
        with open(self.file_path, "r") as usuarios_json:
            usuarios = json.load(usuarios_json)
        for u in usuarios["usuarios"]:
            if u["cod"] == usuario_id:
                return UsuarioModel(
                    cod=u["cod"],
                    usuario=u["usuario"],
                    senha=u["senha"],
                    nome=u["nome"],
                    saldo=u["saldo"],
                    role=u["role"],
                )
        raise Exception("Usuário não encontrado.")

    def get_by_usuario(self, usuario):
        """Busca um usuário pelo nome de usuário."""
        with open(self.file_path, "r") as usuarios_json:
            usuarios = json.load(usuarios_json)
        for u in usuarios["usuarios"]:
            if u["usuario"] == usuario:
                return UsuarioModel(
                    cod=u["cod"],
                    usuario=u["usuario"],
                    senha=u["senha"],
                    nome=u["nome"],
                    saldo=u["saldo"],
                    role=u["role"],
                )
        raise Exception("Usuário não encontrado.")

    def create(self, cod, usuario, senha, nome, saldo, role):
        """Cadastra um novo usuário."""
        with open(self.file_path, "r") as usuarios_json:
            usuarios = json.load(usuarios_json)

        new_usuario = {
            "cod": cod,
            "usuario": usuario,
            "senha": senha,
            "nome": nome,
            "saldo": saldo,
            "role": role,
        }
        usuarios["usuarios"].append(new_usuario)
        usuarios["quantidade"] += 1

        with open(self.file_path, "w") as usuarios_json:
            json.dump(usuarios, usuarios_json, indent=4)

        return UsuarioModel(**new_usuario)

    def update(self, usuario_id, usuario=None, senha=None, nome=None, saldo=None, role=None):
        """Atualiza um usuário existente."""
        with open(self.file_path, "r") as usuarios_json:
            usuarios = json.load(usuarios_json)

        for u in usuarios["usuarios"]:
            if u["cod"] == usuario_id:
                if usuario:
                    u["usuario"] = usuario
                if senha:
                    u["senha"] = senha
                if nome:
                    u["nome"] = nome
                if saldo is not None:  # Permite saldo zero
                    u["saldo"] = saldo
                if role:
                    u["role"] = role

                with open(self.file_path, "w") as usuarios_json:
                    json.dump(usuarios, usuarios_json, indent=4)

                return UsuarioModel(
                    cod=u["cod"],
                    usuario=u["usuario"],
                    senha=u["senha"],
                    nome=u["nome"],
                    saldo=u["saldo"],
                    role=u["role"],
                )

        raise Exception("Usuário não encontrado para atualização.")

    def delete(self, usuario_id):
        """Deleta um usuário existente."""
        with open(self.file_path, "r") as usuarios_json:
            usuarios = json.load(usuarios_json)

        usuarios["usuarios"] = [u for u in usuarios["usuarios"] if u["cod"] != usuario_id]
        usuarios["quantidade"] = len(usuarios["usuarios"])

        with open(self.file_path, "w") as usuarios_json:
            json.dump(usuarios, usuarios_json, indent=4)

        return f"Usuário com ID {usuario_id} foi deletado com sucesso."