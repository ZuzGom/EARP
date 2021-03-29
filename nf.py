from plyer import notification
import webbrowser
#http://13c058b20a8b.ngrok.io/c/jF3GCI2kVcyQzv0v
def idle():
    b, t = 0, "good"
    if b:
        notification.notify(title='Ul wymaga akcji!', 
        message=t)
    else:
        notification.notify(title='Twój ul jest bezpiczny!', 
        message='poprzez Elektorniczny Asystent Rodziny Pszczelej')
def reg():
    webbrowser.open('https://notify.run/c/mO3yfQmLdbxvMoIj')
