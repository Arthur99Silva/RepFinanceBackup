import json
from model.despesa_model import DespesaModel
from persistence.base_dao import BaseDAO

class DespesaDAO(BaseDAO):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DespesaDAO, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'file_path'):
            self.file_path = "data/Despesa.json"

    def get_all(self):
        """Retorna todas as despesas."""
        despesas_list = []
        try:
            with open(self.file_path, encoding="utf-8") as despesas_json:
                despesas = json.load(despesas_json)
            for d in despesas.get("despesas", []):
                despesas_list.append(
                    DespesaModel(
                        codigo=d.get("codigo", ""),
                        descricao=d.get("descricao", ""),
                        valor=d.get("valor", 0.0),
                        usuario=d.get("usuario", ""),
                        categoria=d.get("categoria", ""),
                        mes_vencimento=d.get("mes_vencimento", 0),
                        ano_vencimento=d.get("ano_vencimento", 0),
                        status=d.get("status", "Pendente")
                    )
                )
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erro ao ler o arquivo de despesas.")
        return despesas_list

    def get_by_id(self, despesa_id):
        """Busca uma despesa por ID."""
        try:
            with open(self.file_path, encoding="utf-8") as despesas_json:
                despesas = json.load(despesas_json)
            for d in despesas.get("despesas", []):
                if d["codigo"] == despesa_id:
                    return DespesaModel(
                        codigo=d.get("codigo", ""),
                        descricao=d.get("descricao", ""),
                        valor=d.get("valor", 0.0),
                        usuario=d.get("usuario", ""),
                        categoria=d.get("categoria", ""),
                        mes_vencimento=d.get("mes_vencimento", 0),
                        ano_vencimento=d.get("ano_vencimento", 0),
                        status=d.get("status", "Pendente")
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erro ao buscar despesa por ID.")
        raise Exception("Despesa não encontrada.")

    def create(self, descricao, usuario, valor, mes_vencimento, ano_vencimento, categoria=""):
        """Cadastra uma nova despesa."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as despesas_json:
                despesas = json.load(despesas_json)

            new_despesa = {
                "codigo": str(despesas.get("currentId", 0) + 1),
                "descricao": descricao,
                "valor": valor,
                "usuario": usuario,
                "categoria": categoria,
                "mes_vencimento": mes_vencimento,
                "ano_vencimento": ano_vencimento,
                "status": "Pendente",
            }
            despesas.setdefault("despesas", []).append(new_despesa)
            despesas["currentId"] = int(new_despesa["codigo"])

            with open(self.file_path, "w", encoding="utf-8") as despesas_json:
                json.dump(despesas, despesas_json, indent=4)

            return DespesaModel(**new_despesa)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao criar despesa: {e}")

    def update(self, despesa_id, descricao=None, valor=None, usuario=None, mes_vencimento=None, ano_vencimento=None, categoria=None):
        """Atualiza uma despesa existente."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as despesas_json:
                despesas = json.load(despesas_json)

            for d in despesas["despesas"]:
                if d["codigo"] == despesa_id:
                    if descricao:
                        d["descricao"] = descricao
                    if valor:
                        d["valor"] = valor
                    if usuario:
                        d["usuario"] = usuario
                    if categoria is not None:
                        d["categoria"] = categoria
                    if mes_vencimento:
                        d["mes_vencimento"] = int(mes_vencimento)
                    if ano_vencimento:
                        d["ano_vencimento"] = int(ano_vencimento)

                    with open(self.file_path, "w", encoding="utf-8") as despesas_json:
                        json.dump(despesas, despesas_json, indent=4)

                    return DespesaModel(
                        codigo=d.get("codigo", ""),
                        descricao=d.get("descricao", ""),
                        valor=d.get("valor", 0.0),
                        usuario=d.get("usuario", ""),
                        categoria=d.get("categoria", ""),
                        mes_vencimento=d.get("mes_vencimento", 0),
                        ano_vencimento=d.get("ano_vencimento", 0),
                        status=d.get("status", "Pendente")
                    )
        except (FileNotFoundError, KeyError, json.JSONDecodeError, ValueError) as e:
            print(f"Erro ao atualizar despesa: {e}")

        raise Exception("Despesa não encontrada para atualização.")

    def delete(self, despesa_id):
        """Deleta uma despesa existente."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as despesas_json:
                despesas = json.load(despesas_json)

            despesas["despesas"] = [d for d in despesas["despesas"] if d["codigo"] != despesa_id]
            despesas["quantidade"] = len(despesas["despesas"])

            with open(self.file_path, "w", encoding="utf-8") as despesas_json:
                json.dump(despesas, despesas_json, indent=4)

            return f"Despesa com ID {despesa_id} foi deletada com sucesso."
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao deletar despesa: {e}")

        raise Exception("Erro ao deletar despesa.")
