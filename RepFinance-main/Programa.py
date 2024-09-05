from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from view.login_view.login_view import LoginView

class OsiresApp(App):
    user = ObjectProperty(None)
    
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        self.screen_manager = ScreenManager(transition=NoTransition())
        self.screen_manager.add_widget(LoginView(name='login_view'))

        return self.screen_manager

if __name__ == '__main__':
    OsiresApp().run()
