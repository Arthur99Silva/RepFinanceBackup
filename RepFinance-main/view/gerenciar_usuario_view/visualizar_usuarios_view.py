from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.properties import (
    StringProperty,
    NumericProperty,
    BooleanProperty,
    ListProperty,
)
from view.home_view.home_view import HomeView
from kivy.lang import Builder
from controller.usuario_controller import UsuarioController
import json
import re

Builder.load_file("view/gerenciar_usuario_view/visualizar_usuarios_view.kv")


class Usuario(BoxLayout):
    nome = StringProperty("")
    role = StringProperty("")
    usuario = StringProperty("")
    cod = StringProperty("")
    saldo = NumericProperty()
    edit = BooleanProperty(True)
    apagar_callback = None

    def __init__(self, usuario, apagar_callback, edit, **kwargs):
        super().__init__(**kwargs)
        self.nome = usuario.nome
        self.usuario = usuario.usuario
        self.cod = usuario.cod
        self.saldo = usuario.saldo
        self.edit = edit
        roles = []
        if "m" in usuario.role:
            roles.append("Morador")
        if "rc" in usuario.role:
            roles.append("Responsável por contas")
        self.role = str(roles)
        self.apagar_callback = apagar_callback

    pass


class VisualizarUsuariosView(Screen):

    usuario_controller = UsuarioController()
    usuarios = ListProperty([])
    admin_habilitado = True

    def on_enter(self):
        if ("rc" not in App.get_running_app().user.role) and self.admin_habilitado:
            self.ids.panel.remove_widget(self.ids.cadastrar)
            self.admin_habilitado = False

        self.usuarios = self.usuario_controller.get_usuarios()

    def on_usuarios(self, instance, value):
        usuarios_list = self.ids.usuarios_list

        usuarios_list.clear_widgets()

        for usuario in self.usuarios:
            usuarios_list.add_widget(
                Usuario(usuario=usuario, apagar_callback=self.apagar_usuario, edit=not self.admin_habilitado)
            )

    def cadastrar_usuario(self):
        nome = self.ids.nome.text
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        saldo = self.ids.saldo.text
        self.usuarios = self.usuario_controller.cadastrar_usuario(
            nome=nome, usuario=usuario, senha=senha, saldo=saldo
        )
        self.limpar_formulario_cadastro()
        self.ids["panel"].switch_to(self.ids["buscar"])

    def apagar_usuario(self, codigo):
        self.usuarios = self.usuario_controller.apagar_usuario(codigo)

    def buscar_por_nome(self):
        nome_busca = self.ids.nome_buscar.text
        if nome_busca == "":
            self.usuarios = self.usuario_controller.get_usuarios()
            return

        self.usuarios = self.usuario_controller.buscar_por_nome(nome_busca)
        
    def limpar_formulario_cadastro(self):
        self.ids.nome.text = ""
        self.ids.usuario.text = ""
        self.ids.senha.text = ""
        self.ids.saldo.text = ""

    def voltar(self):
        self.manager.switch_to(HomeView())
