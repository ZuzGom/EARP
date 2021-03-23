from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import notification


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# root = root()
# root = Widget()
def manag(scr):
    # scr.add_widget(MenuScreen(name="menu"))
    scr.add_widget(Ule(name="ule"))
    scr.add_widget(Alert(name="alert"))
    scr.add_widget(Notif(name="arch"))
    scr.add_widget(Sett(name="set"))


global MenuScreen, Ule, Alert, sm

sm = ScreenManager()


class Menu(FloatLayout):
    @staticmethod
    def now(name):
        sm.current = name


class Sett(Screen):
    @staticmethod
    def checkbox_click(value):
        if value is True:
            Window.clearcolor = (40 / 255, 40 / 255, 40 / 255, 1)
        else:
            Window.clearcolor = (250 / 255, 233 / 255, 203 / 255, 1)


class SettingsScreen(Screen):
    pass


class Ule(Screen):
    pass


class Alert(Screen):
    pass


class Notif(Screen):
    pass


# sm = ScreenManager()
# Scr.add_widget(MenuScreen(name="menu"))

class TestApp(App):
    Window.clearcolor = (40 / 255, 40 / 255, 40 / 255, 1)

    def build(self):
        # sm = ScreenManager()
        manag(sm)
        return sm


# buildozer android debug deploy run

try:
    if __name__ == '__main__':
        TestApp().run()
except Exception as ex:

    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title='Coś poszło nie tak ;(', message=err, timeout=20)
    notification.notify(title='Prosimy o wysłanie maila z błędem', message='Dziękujemy za współpracę', timeout=20)
    # email.send(recipient='zuzgom@gmail.com', subject ='Error', text=ex, create_chooser=True)
