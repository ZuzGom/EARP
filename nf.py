from plyer import notification
from bat import check_err
def idle():
    b, t = check_err(1)
    if b:
        notification.notify(title='Ul wymaga akcji!', 
        message=t)
    else:
        notification.notify(title='Twój ul jest bezpiczny!', 
        message='poprzez Elektorniczny Asystent Rodziny Pszczelej')