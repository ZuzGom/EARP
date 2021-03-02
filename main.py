import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
from kivy.core.window import Window
import kivy
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
#from kivy.properties import ObjectProperty, ListProperty
import kivy_garden.contextmenu

Builder.load_file('simple.kv')
#Window.clearcolor = (249, 201, 1, 1)
'''
class Tlo(Label):
    background = ListProperty((0.2, 0.2, 0.2))
'''

class Warstwa(Widget):
    pass

class MyApp(App):
    def build(self):
        self.title = 'EARP'
        
        Window.clearcolor = (250/255,233/255,203/255,1)
        return Warstwa()

if __name__ == '__main__':
    MyApp().run()