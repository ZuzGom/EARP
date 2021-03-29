from plyer import notification
from notify_run import Notify, cli
nf = Notify("http://127.0.0.1")
def idle():
    b, t = 0, "good"
    if b:
        notification.notify(title='Ul wymaga akcji!', 
        message=t)
    else:
        notification.notify(title='Twój ul jest bezpiczny!', 
        message='poprzez Elektorniczny Asystent Rodziny Pszczelej')

def reg():
    #cli.configure(,1)
    
    #.nf.write_config()
    nf.write_config("http://127")

#reg()