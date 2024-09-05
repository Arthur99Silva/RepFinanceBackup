from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.lang import Builder
from controller.despesa_controller import DespesaController
from view.home_view.home_view import HomeView

Builder.load_file("view/gerenciar_despesa_view/visualizar_despesas_view.kv")

class Despesa(BoxLayout):
    codigo = StringProperty("")
    valor = NumericProperty(0)
    usuario = StringProperty("")
    descricao = StringProperty("")
    status = StringProperty("")
    mes = NumericProperty(0)
    ano = NumericProperty(0)
    mes_vencimento = NumericProperty(0)
    ano_vencimento = NumericProperty(0)
    apagar_callback = None
    edit = BooleanProperty(True)

    def __init__(self, despesa, apagar_callback, edit, **kwargs):
        super().__init__(**kwargs)
        self.codigo = despesa.codigo
        self.descricao = despesa.descricao
        self.status = despesa.status

        if isinstance(despesa.usuario, dict):
            self.usuario = despesa.usuario.get('usuario', '')
        else:
            self.usuario = despesa.usuario

        self.valor = despesa.valor
        self.mes_vencimento = despesa.mes_vencimento
        self.ano_vencimento = despesa.ano_vencimento
        self.mes = despesa.mes
        self.ano = despesa.ano
        self.apagar_callback = apagar_callback
        self.edit = edit

class VisualizarDespesasView(Screen):
    despesa_controller = DespesaController()
    despesas = ListProperty([])
    admin_habilitado = True

    def on_enter(self):
        """Atualiza a lista de despesas ao entrar na tela."""
        if ('rc' not in App.get_running_app().user.role) and self.admin_habilitado:
            self.ids.panel.remove_widget(self.ids.cadastrar)
            self.admin_habilitado = False
        
        self.despesas = self.despesa_controller.get_despesas() or []

    def on_despesas(self, instance, value):
        """Atualiza a interface quando a lista de despesas é modificada."""
        despesas_list = self.ids.despesas_list
        despesas_list.clear_widgets()

        for despesa in self.despesas:
            despesas_list.add_widget(
                Despesa(despesa=despesa, apagar_callback=self.apagar_despesa, edit=not self.admin_habilitado)
            )

    def cadastrar_despesa(self):
        """Cadastra uma nova despesa e atualiza a lista."""
        descricao = self.ids.descricao.text
        valor = self.ids.valor.text
        usuario = self.ids.usuario.text
        mes_vencimento = self.ids.mes_vencimento.text
        ano_vencimento = self.ids.ano_vencimento.text

        self.despesas = self.despesa_controller.cadastrar_despesa(
            descricao=descricao,
            usuario=usuario,
            valor=valor,
            mes_vencimento=mes_vencimento,
            ano_vencimento=ano_vencimento,
            categoria=""
        ) or []

        self.limpar_formulario_cadastro()
        self.ids["panel"].switch_to(self.ids["buscar"])

    def apagar_despesa(self, codigo):
        """Apaga uma despesa e atualiza a lista."""
        self.despesas = self.despesa_controller.apagar_despesa(codigo) or []

    def buscar_por_descricao(self):
        """Busca despesas por descrição e atualiza a lista."""
        descricao_busca = self.ids.descricao_buscar.text

        self.despesas = self.despesa_controller.buscar_por_descricao(descricao_busca) or []

    def limpar_formulario_cadastro(self):
        """Limpa os campos de entrada após o cadastro."""
        self.ids.descricao.text = ""
        self.ids.valor.text = ""
        self.ids.usuario.text = ""
        self.ids.mes_vencimento.text = ""
        self.ids.ano_vencimento.text = ""

    def voltar(self):
        """Retorna para a tela anterior."""
        self.manager.switch_to(HomeView())
