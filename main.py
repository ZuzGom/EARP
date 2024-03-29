#!/usr/bin/env python
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from plyer import notification
from gardenmat.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import datetime

from kivy.core.image import Image
from kivy.uix.image import Image as image
import webbrowser

try:
    from bat import *
    from xlsxwriter import Workbook

except Exception as ex:
    print(ex)
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    print(err)
    notification.notify(title=err, message=err[50:], timeout=20)
    push_alert(0,0,err)
    
lista_uli=[0,1,2,3,4]

def temp():
    return []
def manag(scr):
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
    date=[]
    #print(dane)
    for x in dane:
        
        pltem1.append(float(x[1]))
        pltem2.append(float(x[2]))
        plhum.append(float(x[3]))
        plwg.append(float(x[4]))
        date.append(datetime(*x[0][0:6]))
        

    ax.patch.set_facecolor('#151515')
    #ax.patch.set_alpha(0.2)
    ax.tick_params(colors='white', which='both', labelsize='xx-large')
    plt.plot(date, pltem1, 'o', markersize=1, label='Temp.Zew')
    
    plt.plot(date, pltem2, 'o', markersize=1, label='Temp.Wew')
    plt.plot(date, plhum, 'o', markersize=1, label='Wilgotność')
    plt.plot(date, plwg, 'o', markersize=1,label='Waga')
    
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #      fancybox=True, shadow=True, ncol=3)
    plt.gcf().autofmt_xdate()
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=4, mode="expand", borderaxespad=0,fontsize='xx-large')

global MenuScreen, Ule, Alert, sm, czas

sm = ScreenManager(transition=NoTransition())

class Err(Label):
    pass
class Maly(image):
    pass
class Menu(FloatLayout):
    texture = Image('image/st.png').texture
    @staticmethod
    def now(name):
        sm.current = name
        

class Ul(GridLayout):
    data, temp, waga, humi = "00-00-0000 \n 00:00:00","0","0","0"
    
    
    def __init__(self,ul_id):
        super(Ul,self).__init__()
        self.ul_id=ul_id
    
    def update(self):
        #inf =get_inf()
        dat= str(datetime.now())
        dat = dat[:10]+'\n'+dat[11:]
        inf = dat,"0","0","0"
        self.ids.dat.text, self.ids.tem.text, self.ids.wei.text, self.ids.hum.text, = inf
        self.data, self.waga, self.temp, self.humi=inf

        


class Ule(Screen):
    ul_obiekt=[]
    #data, temp, waga, humi = get_inf()
    

    data, temp, waga, humi = "00-00-0000 \n 00:00:00","0","0","0"
    il = len(lista_uli) + 1
    def go(self):
        for i in range(self.il-1):
            self.ul_obiekt[i].update()

    def __init__(self,**kwargs):
        super(Ule,self).__init__(**kwargs)
        for x in lista_uli:
            temp = Ul(x)
            self.ul_obiekt.append(temp)                  
            self.ids.cialo.add_widget(temp)
        self.ids.cialo.add_widget(Label(size_hint=(1,0.5) ))
    def up(self):
        global ul_id
        inf=get_inf()
        self.ids.dat.text, self.ids.tem.text, self.ids.wei.text, self.ids.hum.text, = inf
        #self.ids.dat.text=str(datetime.datetime.now())
        if inf[0]=="00-00-0000 \n 00:00:00":
            self.ids.cialo.clear_widgets()
            self.ids.cialo.add_widget(image(source="image/Batis_Pszczola.png"))
            self.ids.cialo.add_widget(Button(text="^\nSprawdź swoje połączenie!"))
        else:
            self.ids.cialo.clear_widgets()


class Alert(Screen):   
    
    def up(self):
        def op(instance):
            webbrowser.open(track()+'earp')
    
        dane = get_err()
        self.ids.eror.clear_widgets()
        for i in range(len(dane)):
            tekst = str(dane[i][0]) + '\nKod:' + str(dane[i][2]) + '\n' + str(dane[i][3]) 
            log = Err(text=tekst)
            box = BoxLayout(orientation='horizontal') 
            box.add_widget(Maly())
            box.add_widget(log)
            self.ids.eror.add_widget(box)
        but =Button(text="Więcej", size_hint=(1, None))
        for _ in range(len(dane),5):
            self.ids.eror.add_widget(Err(text=" "))
        but.bind(on_release=op)
        self.ids.eror.add_widget(but)
        self.ids.eror.add_widget(Err(text=" "))
        
class Raport(Popup):
    def raport(self):
        self.ids.log.text = "To może trochę zająć"
        try:
            rok = int(self.ids.Y.text)
            mies = int(self.ids.M.text)
            dzien = int(self.ids.D.text)
            dane = get_all(rok,mies,dzien)
            dane.insert(0,"Date, Temperature, AdditionalTemperature, Humidity, Weight, Water, Sound, AccelerationX, AccelerationY, AccelerationZ, RotationX, RotationY, RotationZ".split(","))
        except Exception as err:
            notification.notify(title="Nieprawidłowy format daty", message=err[50:], timeout=20)
            return 1
        
        path = '/storage/emulated/0/Download/'
        try:
            with Workbook('/storage/emulated/0/Download/Raport_'+str(datetime.now())+'.xlsx') as book:
                sheet = book.add_worksheet()
                for row, data in enumerate(dane):
                    try:
                        data[0]=str(datetime(*data[0][0:6]))
                    except TypeError:
                        data[0]=str(data[0])                    
                    sheet.write_row(row, 0, data)

        except:
            with Workbook('Raport_'+str(datetime.now())+'.xlsx') as book:
                sheet = book.add_worksheet()
                for row, data in enumerate(dane):                                      
                    try:
                        data[0]=str(datetime(*data[0][0:6]))
                    except TypeError:
                        data[0]=str(data[0])                    
                    sheet.write_row(row, 0, data)
        self.ids.log.text = "Zapisane!"

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

class Comit(Popup):
    def send(self):
        push_alert(0,1,str(self.ids.alert.text))

class Sett(Screen):
    def op(self):
        webbrowser.open(track()+'earp')
    @staticmethod
    def checkbox_click(value):
        if value is True:
            Window.clearcolor = (40 / 255, 40 / 255, 40 / 255, 1)
        else:
            Window.clearcolor = (255 / 255, 255 / 255, 235 / 255, 1)
    stts="Nieaktywne"


try:
    #ule = [[x] for x in get_ule('001')]
    fig = plt.figure()
    fig.patch.set_facecolor('#202020')
    #fig.patch.set_alpha(0.3)
    ax = fig.add_subplot(111)
    rysuj(temp())
except Exception as ex:
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    notification.notify(title=err, message=err[50:], timeout=20)

class Wykres(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super(Wykres, self).__init__(plt.gcf(), **kwargs)



class TestApp(App):
    Window.clearcolor = (40 / 255, 40 / 255, 40 / 255, 1)

    def build(self):
        manag(sm)       
        return sm

#if __name__ == '__main__':
    #TestApp().run()
# buildozer android debug deploy run

try:
    if __name__ == '__main__':
        TestApp().run()
        
        
      
except Exception as ex:
    print(ex)
    err = '{}: {})'.format(ex.__class__.__name__, ex)
    print(err)
    push_alert(0,0,err)
    notification.notify(title=err, message=err[50:], timeout=20)
    #notification.notify(title='Prosimy o wysłanie maila z błędem', message='Dziękujemy za współpracę', timeout=20)
    # email.send(recipient='zuzgom@gmail.com', subject ='Error', text=ex, create_chooser=True)
   