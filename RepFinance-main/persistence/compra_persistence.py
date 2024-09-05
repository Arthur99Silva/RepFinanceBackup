import json
from model.compra_model import CompraModel
from persistence.usuario_persistence import UsuarioPersistence

ENTIDADE = "Compra"


class CompraPersistence:

    # def get_by_usuario(self, usuario = None):
    #     if usuario == None:
    #         raise Exception("Informe um usuário ou um Id para retornar um usuário.")

    #     with open('data/Usuario.json') as usuarios_json:
    #         usuarios = json.load(usuarios_json)

    #     for u in usuarios['usuarios']:
    #         if u['usuario'] == usuario:
    #             return UsuarioModel(cod=u['cod'], usuario=u['usuario'], senha=u['senha'], nome=u['nome'], saldo=u['saldo'], role=u['role'])

    #     raise Exception("Usuário não encontrado.")

    def get_compras(self):
        compras_list = []

        with open(f"data/{ENTIDADE}.json", encoding="utf-8") as compras_json:
            compras = json.load(compras_json)

        for c in compras["compras"]:
            compras_list.append(
                CompraModel(
                    codigo=c["codigo"],
                    usuario=c["usuario"]["usuario"],
                    descricao=c["descricao"],
                    status=c["status"],
                    valor=c["valor"],
                )
            )

        return compras_list

    def cadastrar_compra(self, descricao, usuario, valor):
        with open(f"data/{ENTIDADE}.json", "r", encoding="utf-8") as compras_json:
            compras = json.load(compras_json)

        usuario_persistence = UsuarioPersistence()
        usuario = usuario_persistence.get_by_usuario(usuario=usuario)

        new_compra = {
            "codigo": str(compras["currentId"] + 1),
            "usuario": {
                "cod": usuario.cod,
                "usuario": usuario.usuario,
                "senha": usuario.senha,
                "nome": usuario.nome,
                "saldo": usuario.saldo,
                "role": usuario.role,
            },
            "descricao": descricao,
            "valor": valor,
            "status": "pendente",
        }

        compras["compras"].append(new_compra)
        compras["quantidade"] = compras["quantidade"] + 1
        compras["currentId"] = compras["currentId"] + 1

        with open(f"data/{ENTIDADE}.json", "w") as compras_json:
            json.dump(compras, compras_json, indent=4)

        return [
            CompraModel(
                codigo=c["codigo"],
                usuario=c["usuario"]["usuario"],
                descricao=c["descricao"],
                valor=c["valor"],
                status=c["status"],
            )
            for c in compras["compras"]
        ]

    def apagar_compra(self, codigo):
        new_compras = []

        with open(f"data/{ENTIDADE}.json", "r") as compras_json:
            compras = json.load(compras_json)

        for c in compras["compras"]:
            if c["codigo"] == codigo:
                continue
            new_compras.append(c)
        compras["compras"] = new_compras[:]
        compras["quantidade"] = int(compras["quantidade"]) - 1

        with open(f"data/{ENTIDADE}.json", "w") as compras_json:
            json.dump(compras, compras_json, indent=4)

        return [
            CompraModel(
                codigo=c["codigo"],
                usuario=c["usuario"]["usuario"],
                descricao=c["descricao"],
                valor=c["valor"],
                status=c["status"],
            )
            for c in new_compras
        ]

    def get_by_descricao(self, descricao):
        new_compras = []
        if descricao == "":
            return self.get_compras()

        with open(f"data/{ENTIDADE}.json") as compra_json:
            compras = json.load(compra_json)

        for c in compras["compras"]:
            if descricao.upper() in c["descricao"].upper():
                new_compras.append(
                    CompraModel(
                        codigo=c["codigo"],
                        usuario=c["usuario"]["usuario"],
                        descricao=c["descricao"],
                        valor=c["valor"],
                        status=c["status"],
                    )
                )
        return new_compras
