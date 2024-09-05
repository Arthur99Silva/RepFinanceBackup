from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.lang import Builder
from controller.compra_controller import CompraController
from view.home_view.home_view import HomeView

Builder.load_file("view/gerenciar_compra_view/visualizar_compras_view.kv")

class Compra(BoxLayout):
    codigo = StringProperty("")
    valor = NumericProperty(0)
    usuario = StringProperty("")
    descricao = StringProperty("")
    status = StringProperty("")
    edit = BooleanProperty(True)
    apagar_callback = None

    def __init__(self, compra, apagar_callback, edit, **kwargs):
        super().__init__(**kwargs)
        self.codigo = compra.codigo
        self.valor = compra.valor
        self.usuario = compra.usuario
        self.descricao = compra.descricao
        self.status = compra.status
        self.edit = edit
        self.apagar_callback = apagar_callback

class VisualizarComprasView(Screen):
    compra_controller = CompraController()
    compras = ListProperty([])
    admin_habilitado = True

    def on_enter(self):
        """Atualiza a lista de compras ao entrar na tela."""
        if ("rc" not in App.get_running_app().user.role) and self.admin_habilitado:
            self.ids.panel.remove_widget(self.ids.cadastrar)
            self.admin_habilitado = False

        self.compras = self.compra_controller.get_compras()

    def on_compras(self, instance, value):
        """Atualiza a interface quando a lista de compras é modificada."""
        compras_list = self.ids.compras_list
        compras_list.clear_widgets()

        for c in self.compras:
            compras_list.add_widget(
                Compra(
                    compra=c,
                    apagar_callback=self.apagar_compra,
                    edit=not self.admin_habilitado
                )
            )

    def cadastrar_compra(self):
        """Cadastra uma nova compra e atualiza a lista."""
        descricao = self.ids.descricao.text
        usuario = self.ids.usuario.text
        valor = float(self.ids.valor.text)

        self.compras = self.compra_controller.cadastrar_compra(descricao, usuario, valor)

        self.ids.descricao.text = ""
        self.ids.usuario.text = ""
        self.ids.valor.text = ""

    def apagar_compra(self, codigo):
        """Apaga uma compra e atualiza a lista."""
        self.compras = self.compra_controller.apagar_compra(codigo)

    def buscar_por_descricao(self, descricao_buscar):
        """Busca compras por descrição e atualiza a lista."""
        if descricao_buscar == "":
            self.compras = self.compra_controller.get_compras()
        else:
            self.compras = self.compra_controller.buscar_por_descricao(descricao_buscar)

    def voltar(self):
        """Retorna para a tela anterior."""
        self.manager.switch_to(HomeView())

    def atualizar_compra(self, codigo, nova_descricao, novo_valor):
        """Atualiza uma compra existente com novos dados."""
        self.compra_controller.update_compra(codigo, nova_descricao, novo_valor)
        self.compras = self.compra_controller.get_compras()

    def filtrar_por_usuario(self, usuario):
        """Filtra as compras por um usuário específico."""
        self.compras = self.compra_controller.get_by_usuario(usuario)
