from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('view/home_view/home_view.kv')

class HomeView(Screen):
    def gerenciar_moradores(self):
        print(App.get_running_app().user.role)
        from view.gerenciar_usuario_view.visualizar_usuarios_view import VisualizarUsuariosView
        self.manager.switch_to(VisualizarUsuariosView(name='visualizar_usuarios_view'))

    def gerenciar_compras(self):
        from view.gerenciar_compra_view.visualizar_compras_view import VisualizarComprasView
        self.manager.switch_to(VisualizarComprasView(name='visualizar_compras_view'))
        
    def gerenciar_despesas(self):
        from view.gerenciar_despesa_view.visualizar_despesas_view import VisualizarDespesasView
        self.manager.switch_to(VisualizarDespesasView(name='visualizar_despesas_view'))
