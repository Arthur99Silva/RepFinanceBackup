import json
from model.despesa_model import DespesaModel
from persistence.usuario_persistence import UsuarioPersistence

ENTIDADE = "Despesa"


class DespesaPersistence:

    # def get_by_usuario(self, usuario = None):
    #     if usuario == None:
    #         raise Exception("Informe um usuário ou um Id para retornar um usuário.")

    #     with open('data/Usuario.json') as usuarios_json:
    #         usuarios = json.load(usuarios_json)

    #     for u in usuarios['usuarios']:
    #         if u['usuario'] == usuario:
    #             return UsuarioModel(cod=u['cod'], usuario=u['usuario'], senha=u['senha'], nome=u['nome'], saldo=u['saldo'], role=u['role'])

    #     raise Exception("Usuário não encontrado.")

    def get_despesas(self):
        with open(f"data/{ENTIDADE}.json", encoding="utf-8") as despesas_json:
            despesas = json.load(despesas_json)

        return [
            DespesaModel(
                codigo=despesa["codigo"],
                descricao=despesa["descricao"],
                status=despesa["status"],
                usuario=despesa["usuario"],
                valor=despesa["valor"],
                mes_vencimento=despesa["mes_vencimento"],
                ano_vencimento=despesa["ano_vencimento"],
                mes=despesa["mes"],
                ano=despesa["ano"],
            )
            for despesa in despesas["despesas"]
        ]

    def cadastrar_despesa(self, despesa):
        with open(f"data/{ENTIDADE}.json", "r", encoding="utf-8") as despesas_json:
            despesas = json.load(despesas_json)

        usuario_persistence = UsuarioPersistence()
        usuario = usuario_persistence.get_by_usuario(usuario=despesa.usuario)

        despesa.usuario = {
            "cod": usuario.cod,
            "usuario": usuario.usuario,
            "senha": usuario.senha,
            "nome": usuario.nome,
            "saldo": usuario.saldo,
            "role": usuario.role,
        }

        despesa.codigo = str(despesas["currentId"] + 1)

        new_despesa = {
            "codigo": despesa.codigo,
            "usuario": despesa.usuario,
            "descricao": despesa.descricao,
            "valor": despesa.valor,
            "status": "pendente",
            "mes": despesa.mes,
            "ano": despesa.ano,
            "mes_vencimento": despesa.mes_vencimento,
            "ano_vencimento": despesa.ano_vencimento,
        }

        despesas["despesas"].append(new_despesa)
        despesas["quantidade"] = len(despesas["despesas"])
        despesas["currentId"] = despesas["currentId"] + 1

        with open(f"data/{ENTIDADE}.json", "w") as despesas_json:
            json.dump(despesas, despesas_json, indent=4)

        return [
            DespesaModel(
                codigo=despesa["codigo"],
                descricao=despesa["descricao"],
                status=despesa["status"],
                usuario=despesa["usuario"],
                valor=despesa["valor"],
                mes_vencimento=despesa["mes_vencimento"],
                ano_vencimento=despesa["ano_vencimento"],
                mes=despesa["mes"],
                ano=despesa["ano"],
            )
            for despesa in despesas["despesas"]
        ]

    def apagar_despesa(self, codigo):

        with open(f"data/{ENTIDADE}.json", "r") as despesas_json:
            despesas = json.load(despesas_json)

        despesas["despesas"] = [
            despesa for despesa in despesas["despesas"] if despesa["codigo"] != codigo
        ]
        
        print(despesas)
        despesas["quantidade"] = len(despesas["despesas"])

        with open(f"data/{ENTIDADE}.json", "w") as despesas_json:
            json.dump(despesas, despesas_json, indent=4)

        return [
            DespesaModel(
                codigo=despesa["codigo"],
                descricao=despesa["descricao"],
                status=despesa["status"],
                usuario=despesa["usuario"],
                valor=despesa["valor"],
                mes_vencimento=despesa["mes_vencimento"],
                ano_vencimento=despesa["ano_vencimento"],
                mes=despesa["mes"],
                ano=despesa["ano"],
            )
            for despesa in despesas["despesas"]
        ]

    def get_by_descricao(self, descricao):
        new_despesas = []
        if descricao == "":
            return self.get_despesas()

        with open(f"data/{ENTIDADE}.json") as despesa_json:
            despesas = json.load(despesa_json)

        for c in despesas["despesas"]:
            if descricao.upper() in c["descricao"].upper():
                new_despesas.append(
                    DespesaModel(
                        codigo=c["codigo"],
                        usuario=c["usuario"]["usuario"],
                        descricao=c["descricao"],
                        valor=c["valor"],
                        status=c["status"],
                    )
                )

        return [
            DespesaModel(
                codigo=despesa["codigo"],
                descricao=despesa["descricao"],
                status=despesa["status"],
                usuario=despesa["usuario"],
                valor=despesa["valor"],
                mes_vencimento=despesa["mes_vencimento"],
                ano_vencimento=despesa["ano_vencimento"],
                mes=despesa["mes"],
                ano=despesa["ano"],
            )
            for despesa in despesas["despesas"]
            if descricao.upper() in despesa["descricao"].upper()
        ]
