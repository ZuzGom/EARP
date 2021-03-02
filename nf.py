from notify import notification

def idle():
    return notification('Ul bezpieczny!', title='EARP')
idle()