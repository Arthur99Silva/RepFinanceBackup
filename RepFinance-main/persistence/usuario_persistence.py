import json
from model.usuario_model import UsuarioModel


class UsuarioPersistence:

    def get_by_usuario(self, usuario=None):
        if usuario == None:
            raise Exception("Informe um usuário ou um Id para retornar um usuário.")

        with open("data/Usuario.json") as usuarios_json:
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

    def get_usuarios(self):
        usuarios_list = []

        with open("data/Usuario.json") as usuarios_json:
            usuarios = json.load(usuarios_json)

        for u in usuarios["usuarios"]:
            usuarios_list.append(
                UsuarioModel(
                    cod=u["cod"],
                    usuario=u["usuario"],
                    senha=u["senha"],
                    nome=u["nome"],
                    saldo=u["saldo"],
                    role=u["role"],
                )
            )

        return usuarios_list

    def cadastrar_usuario(self, nome, usuario, senha, saldo):
        with open("data/Usuario.json", "r") as usuarios_json:
            usuarios = json.load(usuarios_json)

        new_usuario = {
            "cod": str(usuarios["currentId"] + 1),
            "usuario": usuario,
            "senha": senha,
            "nome": nome,
            "saldo": int(saldo),
            "role": ["m"],
        }

        usuarios["usuarios"].append(new_usuario)
        usuarios["quantidade"] = usuarios["quantidade"] + 1
        usuarios["currentId"] = usuarios["currentId"] + 1

        with open("data/Usuario.json", "w") as usuarios_json:
            json.dump(usuarios, usuarios_json, indent=4)

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

    def apagar_usuario(self, cod):
        new_usuarios = []

        with open("data/Usuario.json", "r") as usuarios_json:
            usuarios = json.load(usuarios_json)

        for u in usuarios["usuarios"]:
            if u["cod"] == cod:
                continue
            new_usuarios.append(u)
        usuarios["usuarios"] = new_usuarios[:]
        usuarios["quantidade"] = int(usuarios["quantidade"]) - 1

        with open("data/Usuario.json", "w") as usuarios_json:
            json.dump(usuarios, usuarios_json, indent=4)

        return [
            UsuarioModel(
                cod=u["cod"],
                usuario=u["usuario"],
                senha=u["senha"],
                nome=u["nome"],
                saldo=u["saldo"],
                role=u["role"],
            )
            for u in new_usuarios
        ]

    def get_by_nome(self, nome):
        new_usuarios = []
        if nome == "":
            return self.get_usuarios()

        with open("data/Usuario.json") as usuarios_json:
            usuarios = json.load(usuarios_json)

        for u in usuarios["usuarios"]:
            if nome.upper() in u["nome"].upper():
                new_usuarios.append(
                    UsuarioModel(
                        cod=u["cod"],
                        usuario=u["usuario"],
                        senha=u["senha"],
                        nome=u["nome"],
                        saldo=u["saldo"],
                        role=u["role"],
                    )
                )
        return new_usuarios
