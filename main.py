from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.contextmenu import ContextMenu, ContextMenuItem
from plyer import notification, email

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

#root = root()
#root = Widget()
def Manag(scr):
    #scr.add_widget(MenuScreen(name="menu"))
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
    def checkbox_click(self, instance, value): 
        if value is True: 
            Window.clearcolor = (40/255,40/255,40/255,1) 
        else: 
            Window.clearcolor = (250/255,233/255,203/255,1)

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
        
    
#buildozer android debug deploy run
        
try:
    if __name__ == '__main__':
        TestApp().run()
except Exception as ex:
    
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title='Coś poszło nie tak ;(', message=err, timeout=20)
    notification.notify(title='Prosimy o wysłanie maila z błędem', message='Dziękujemy za współpracę', timeout=20)
    email.send(recipient='zuzgom@gmail.com', subject ='Error', text=ex, create_chooser=True)

