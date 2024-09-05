from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.lang import Builder
from controller.usuario_controller import UsuarioController
from kivy.app import App

Builder.load_file('view/login_view/login_view.kv')

class LoginView(Screen):
    usuario_controller = UsuarioController()
    usuario = StringProperty("alexandrade")
    senha = StringProperty("alex")

    def login(self):
        try:
            usuario = self.usuario_controller.login(self.usuario, self.senha)
            if usuario:
                App.get_running_app().user = usuario
                from view.home_view.home_view import HomeView
                self.manager.switch_to(HomeView(name='home_view'))
            else:
                self.add_widget(Label(text="Credenciais inválidas"))
        except Exception as e:
            print(e)
            self.add_widget(Label(text="Credenciais inválidas", color=(0, 0, 0, 1)))
