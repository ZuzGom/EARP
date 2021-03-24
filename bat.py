from datetime import datetime, timedelta
from mysql.connector import connect, Error

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def get_inf(id):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="ekonomik.atthost24.pl",
            user="18013_earp",
            password="earp.123",
        )
    except Error as e:
        notification.notify(title=e, message=e[50:])

    #ważna funkcja służy do pobierania informacji o aktualnych właściwościach ula o danym id

    select_temp = "SELECT TOP 1 temperatura FROM dane"
    temp = execute_read_query(connection, select_temp)

    select_waga = "SELECT TOP 1 masa FROM dane"
    waga =  execute_read_query(connection, select_waga)

    select_humi = "SELECT TOP 1 wilgotnosc FROM dane"
    humi = execute_read_query(connection, select_humi)
    #Jeszcze musze wyciagnac date
    return temp+"°C", waga+ "kg", humi+"%"

def data():
    #funkcja dla mnie, sprawdza czy sie updatuje
    now = datetime.now()
    return str(now)

'''
def get_all(id, time):
    ''
    przyszlosciowa funkcja
    zwraca listę dwuwymiarową z danymi od danej daty do obecnego czasu
   
    date = datetime.now()-timedelta(minutes=time)
    #od tej daty ^
    #wiem, jestem wspaniala, ze to za ciebie zrobilam nie musisz dziekowac

    tab = [['77112020-01-17',' 18:48:09',' 24',' 54',' 0'],
    ['77212020-01-17',' 18:48:14',' 23.2',' 55',' 0'],
    ['77312020-01-17',' 18:48:19',' 23.8',' 59',' 0'],
    ['77412020-01-17',' 18:48:24',' 23.8',' 56',' 0'],
    ['77512020-01-17',' 18:48:29',' 23.9',' 54',' 0'],
    ['77612020-01-17',' 18:48:34',' 23.2',' 54',' 0']]
    return tab


#TEGO POD SPODEM NA RAZIE NIE RÓB

def get_ule(id):
    
    ta przyszłościowa funkcja służy do pobierania informacji z tabli 'user' z indeksu ule
    taki indeks trzeba dopiero stworzyć
    lista ule zawiera indeksy uli przypisane do id użytkownika
    
    ule = [1,2]
    return ule

def push_err(txt):
    mess = txt
    
    ta funkcja służy do poinformowania nas o errorach
    pomyślałam, że skoro ule mówią nam, że się źle czują to apka również może
    pushniesz wiadomość txt z id_ula 'U' (jak user) i z kodem do ustalenia
    do tabeli alerty (którą trzeba stworzyć)
    

def check_err(id):  #to chcę na zaraz
    
    sprawdza ostatni stan stan ula dla jego id z tabeli alerty, 
    jesli nie ma erroru zwraca w ciagu ostatnich 5 minut daje False
    
    if id == 1:
        return False, 'good'
    if id == 0:
        return True, 'bad: error type'

def get_err(id):
    
    zwraca ostatnie 10 errorów dla dane id ula
    
    tab = [['2020-01-17; 18:48:09','E01', 'Ziąb'], ['2020-01-17; 18:48:09','E02', 'Miód'], 
    ['2020-01-17; 18:48:09','E00', 'Nieznany błąd'], 
    ['2020-01-17; 18:48:09','E01', 'Ziąb'], ['2020-01-17; 18:48:09','E03', 'Ucieczka']]
    return tab

'''
