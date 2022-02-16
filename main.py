import kivy

from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivy.app import App, Builder
from kivy.core.window import Window

Builder.load_string(open("main.kv", encoding="utf-8").read(), rulesonly=True)


class MococaCRUD(App):
    def build(self):
        App.title = "Cadastro de Bovinos"
        Window.size = (320, 480)
        return sm


class Login(Screen):
    ...


class Main(Screen):
    ...


class CadUser(Screen):
    ...

class EsqSenha(Screen):
    ...


class CadBov(Screen):
    ...
class RelGeral(Screen):
    ...



sm = ScreenManager(transition=WipeTransition())
sm.add_widget(Login(name='Login'))
sm.add_widget(Main(name='Main'))
sm.add_widget(CadUser(name='CadUser'))
sm.add_widget(EsqSenha(name='EsqSenha'))
sm.add_widget(CadBov(name='CadBov'))
sm.add_widget(RelGeral(name='RelGeral'))
sm.current = "Login"

MococaCRUD().run()
