from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import notification
from threading import Thread
try:
    from bat import *
except Exception as ex:

    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title=err, message=err[50:], timeout=20)
threads=[]
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# root = root()
# root = Widget()

class MyClass(object):
    def __init__(self, a=1):
        super(MyClass, self).__init__()
        self.a_min = 0
        self.a_max = 100
        self.a = a

    def _get_a(self):
        return self._a
    def _set_a(self, value):
        if value < self.a_min or value > self.a_max:
            raise ValueError('a out of bounds')
        self._a = value
    a = property(_get_a, _set_a)

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


class Ule(Screen):
    data, temp, waga, humi = get_inf(1)

class Alert(Screen):   
    czas = data()
    
    def up(self):
        czas = data()
        return czas


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
        t = Thread(target=TestApp().run())
        t.start()
        threads.append(t)
        print('ye')
except Exception as ex:

    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title=err, message=err[50:], timeout=20)
    #notification.notify(title='Prosimy o wysłanie maila z błędem', message='Dziękujemy za współpracę', timeout=20)
    # email.send(recipient='zuzgom@gmail.com', subject ='Error', text=ex, create_chooser=True)
