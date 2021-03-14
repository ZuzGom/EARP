from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.contextmenu import ContextMenu, ContextMenuItem
from plyer import notification

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

#root = root()
#root = Widget()
def Manag(scr):
    scr.add_widget(MenuScreen(name="menu"))
    scr.add_widget(Ule(name="ule"))
    scr.add_widget(Alert(name="alert"))
    scr.add_widget(Notif(name="arch"))

global MenuScreen, Ule, Alert, sm

sm = ScreenManager()

class Menu(Widget):
    @staticmethod   
    def now(name):
        sm.current = name

class MenuScreen(Screen):
    pass
    

class SettingsScreen(Screen):
    pass
class Ule(Screen):
    pass
class Alert(Screen):
    def idle(self):
        notification.notify(title='Twój ul jest bezpiczny!', 
        message='poprzez Elektorniczny Asystent Rodziny Pszczelej')
    
class Notif(Screen):
    pass

#sm = ScreenManager()
#Scr.add_widget(MenuScreen(name="menu"))

class TestApp(App):
    Window.clearcolor = (40/255,40/255,40/255,1)
    def build(self):
        #sm = ScreenManager()
        Manag(sm)
        return sm
        
    

        

if __name__ == '__main__':
    TestApp().run()