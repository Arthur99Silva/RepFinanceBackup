import json
from persistence.base_dao import BaseDAO
from persistence.usuario_dao import UsuarioDAO
from model.compra_model import CompraModel

class CompraDAO(BaseDAO):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CompraDAO, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'file_path'):
            self.file_path = "data/Compra.json"
            self.usuario_dao = UsuarioDAO()

    def get_all(self):
        """Retorna todas as compras."""
        compras_list = []
        with open(self.file_path, encoding="utf-8") as compras_json:
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

    def get_by_id(self, compra_id):
        """Busca uma compra por ID."""
        with open(self.file_path, encoding="utf-8") as compras_json:
            compras = json.load(compras_json)
        for c in compras["compras"]:
            if c["codigo"] == compra_id:
                return CompraModel(
                    codigo=c["codigo"],
                    usuario=c["usuario"]["usuario"],
                    descricao=c["descricao"],
                    status=c["status"],
                    valor=c["valor"],
                )
        raise Exception("Compra não encontrada.")

    def create(self, descricao, usuario, valor):
        """Cadastra uma nova compra."""
        with open(self.file_path, "r", encoding="utf-8") as compras_json:
            compras = json.load(compras_json)

        usuario_model = self.usuario_dao.get_by_usuario(usuario=usuario)

        new_compra = {
            "codigo": str(compras["currentId"] + 1),
            "usuario": {
                "cod": usuario_model.cod,
                "usuario": usuario_model.usuario,
                "senha": usuario_model.senha,
                "nome": usuario_model.nome,
                "saldo": usuario_model.saldo,
                "role": usuario_model.role,
            },
            "descricao": descricao,
            "status": "Pendente",
            "valor": valor,
        }
        compras["compras"].append(new_compra)
        compras["currentId"] += 1

        with open(self.file_path, "w", encoding="utf-8") as compras_json:
            json.dump(compras, compras_json, indent=4)

        return CompraModel(**new_compra)

    def update(self, compra_id, descricao=None, usuario=None, valor=None, status=None):
        """Atualiza uma compra existente."""
        with open(self.file_path, "r", encoding="utf-8") as compras_json:
            compras = json.load(compras_json)

        for c in compras["compras"]:
            if c["codigo"] == compra_id:
                if descricao:
                    c["descricao"] = descricao
                if usuario:
                    usuario_model = self.usuario_dao.get_by_usuario(usuario=usuario)
                    c["usuario"] = {
                        "cod": usuario_model.cod,
                        "usuario": usuario_model.usuario,
                        "senha": usuario_model.senha,
                        "nome": usuario_model.nome,
                        "saldo": usuario_model.saldo,
                        "role": usuario_model.role,
                    }
                if valor:
                    c["valor"] = valor
                if status:
                    c["status"] = status

                with open(self.file_path, "w", encoding="utf-8") as compras_json:
                    json.dump(compras, compras_json, indent=4)

                return CompraModel(
                    codigo=c["codigo"],
                    usuario=c["usuario"]["usuario"],
                    descricao=c["descricao"],
                    status=c["status"],
                    valor=c["valor"],
                )

        raise Exception("Compra não encontrada para atualização.")

    def delete(self, compra_id):
        """Deleta uma compra existente."""
        with open(self.file_path, "r", encoding="utf-8") as compras_json:
            compras = json.load(compras_json)

        compras["compras"] = [c for c in compras["compras"] if c["codigo"] != compra_id]
        compras["quantidade"] = len(compras["compras"])

        with open(self.file_path, "w", encoding="utf-8") as compras_json:
            json.dump(compras, compras_json, indent=4)

        return f"Compra com ID {compra_id} foi deletada com sucesso."

    def get_by_usuario(self, usuario):
        """Busca compras associadas a um usuário específico."""
        compras_list = []
        with open(self.file_path, encoding="utf-8") as compras_json:
            compras = json.load(compras_json)
        for c in compras["compras"]:
            if c["usuario"]["usuario"] == usuario:
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
