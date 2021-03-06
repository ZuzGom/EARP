import kivy
kivy.require('1.0.7')
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
#from kivy.uix.label import Label
#from kivy.uix.popup import Popup

try:
    import kivy_garden.contextmenu
    from plyer import notification
    class Warstwa(Widget):
        def idle(self):
            notification.notify(title='Twój ul jest bezpiczny!', message='poprzez Elektorniczny Asystent Rodziny Pszczelej')
        pass
    class TestApp(App):
        Window.clearcolor = (250/255,233/255,203/255,1)
        #Window.clearcolor = (40/255,40/255,40/255,1)
        def build(self):
            #self.theme_cls.primary_palette = "Yellow"
            #self.theme_cls.primary_hue = "100"
            #self.theme_cls.theme_style = "Dark"
            return Warstwa()

    # buildozer android debug deploy run
    if __name__ == '__main__':
        TestApp().run()
except Exception as ex:
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title='Coś poszło nie tak ;(', message=err, timeout=20)
    
