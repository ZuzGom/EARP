import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy_garden.contextmenu


class MyApp(App):
    def build(self):
        self.title = 'Simple context menu example'
        return Builder.load_file('menu.kv')

    def say_hello(self, text):
        print(text)
        self.root.ids['context_menu'].hide()


if __name__ == '__main__':
    MyApp().run()