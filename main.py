#!/usr/bin/env python

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from plyer import notification
#from threading import Thread
from gardenmat.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from bat import *
from kivy.core.image import Image


'''
try:
    
except Exception as ex:

    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title=err, message=err[50:], timeout=20)
'''

#threads=[]
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# root = root()
# root = Widget()


'''
class Klasa(object):
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
'''

def manag(scr):
    # scr.add_widget(MenuScreen(name="menu"))
    scr.add_widget(Ule(name="ule"))
    scr.add_widget(Alert(name="alert"))
    scr.add_widget(Notif(name="arch"))
    scr.add_widget(Sett(name="set"))


def rysuj(func):
    dane = func
    pltem1=[]
    pltem2=[]
    plwg=[]
    plhum=[]
    #print(dane)
    for x in dane:
        pltem1.append(float(x[2]))
        pltem2.append(float(x[3]))
        plhum.append(float(x[4]))
        plwg.append(float(x[5]))
    #print(plhum)
    #print(plwg)
    ax.patch.set_facecolor('#151515')
    #ax.patch.set_alpha(0.2)
    ax.tick_params(colors='white', which='both', labelsize='xx-large')
    plt.plot(pltem1, label='Temp.Zew')
    plt.plot(pltem2, label='Temp.Wew')
    plt.plot(plhum, label='Wilgotność')
    plt.plot(plwg, label='Waga')
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #      fancybox=True, shadow=True, ncol=3)

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=4, mode="expand", borderaxespad=0,fontsize='xx-large')

global MenuScreen, Ule, Alert, sm, czas

sm = ScreenManager(transition=NoTransition())


class Menu(FloatLayout):

    texture = Image('image/st.png').texture
    @staticmethod
    def now(name):
        sm.current = name
        #Notif.init(self)
        

class Sett(Screen):
    @staticmethod
    def checkbox_click(value):
        if value is True:
            Window.clearcolor = (40 / 255, 40 / 255, 40 / 255, 1)
        else:
            Window.clearcolor = (255 / 255, 255 / 255, 235 / 255, 1)
    stts="Nieaktywne"


class Ule(Screen):
    
    data, temp, waga, humi = get_inf()
    def up(self):
        global ul_id
        self.ids.dat.text, self.ids.tem.text, self.ids.wei.text, self.ids.hum.text, = get_inf()

class Alert(Screen):   
    czas = data()
    
    def up(self):
        czas = data()
        self.ids.tim.text = czas

class Notif(Screen):
    
    def init(self):
        self.ids.dropdown.dismiss()
    def updt(self,text, time):
        self.ids.dropdown.select(text)
        
        self.ids.wykres.clear_widgets()
        ax.clear()
        
        rysuj(get_all(time))
        
        
        self.ids.wykres.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    def godzina(self,text):
        self.ids.dropdown.select(text)
        
        self.ids.wykres.clear_widgets()
        ax.clear()
        
        rysuj(get_all_hour())
        
        self.ids.wykres.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    
    def dzien(self,text):
        self.ids.dropdown.select(text)
        
        self.ids.wykres.clear_widgets()
        ax.clear()
        
        rysuj(get_all_day())
        
        self.ids.wykres.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    def miesiac(self,text):
        self.ids.dropdown.select(text)
        
        self.ids.wykres.clear_widgets()
        ax.clear()
        
        rysuj(get_all_month())
        
        self.ids.wykres.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    def rok(self,text):
        self.ids.dropdown.select(text)
        
        self.ids.wykres.clear_widgets()
        ax.clear()
        
        rysuj(get_all_year())
        
        self.ids.wykres.add_widget(FigureCanvasKivyAgg(plt.gcf()))


try:
    #ule = [[x] for x in get_ule('001')]
    fig = plt.figure()
    fig.patch.set_facecolor('#202020')
    #fig.patch.set_alpha(0.3)
    ax = fig.add_subplot(111)
    rysuj(get_all(100))
except Exception as ex:
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title=err, message=err[50:], timeout=20)

class Wykres(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super(Wykres, self).__init__(plt.gcf(), **kwargs)


# sm = ScreenManager()
# Scr.add_widget(MenuScreen(name="menu"))

class TestApp(App):
    Window.clearcolor = (40 / 255, 40 / 255, 40 / 255, 1)

    def build(self):
        # sm = ScreenManager()
        #Notif.ids.wykres.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        manag(sm)
        return sm


# buildozer android debug deploy run

try:
    if __name__ == '__main__':
        TestApp().run()
        '''
        t = Thread(target=TestApp().run())
        t.start()
        threads.append(t)
        print('ye')
        '''
except Exception as ex:
    print(ex)
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    print(err)
    
    notification.notify(title=err, message=err[50:], timeout=20)
    #notification.notify(title='Prosimy o wysłanie maila z błędem', message='Dziękujemy za współpracę', timeout=20)
    # email.send(recipient='zuzgom@gmail.com', subject ='Error', text=ex, create_chooser=True)