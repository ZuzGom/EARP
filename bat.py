from mysql.connector import connect, Error

try:
    with connect(
        host="ekonomik.atthost24.pl",
        user="18013_earp",
        password="earp.123",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

def push_err(txt):
    mess = txt
    '''
    ta funkcja służy do poinformowania nas o errorach
    pomyślałam, że skoro ule mówią nam, że się źle czują to apka również może
    pushniesz wiadomość txt z id_ula 'U' (jak user) i z kodem do ustalenia
    do tabeli alerty (którą trzeba stworzyć)
    '''

def get_ule(id):
    '''
    ta przyszłościowa funkcja służy do pobierania informacji z tabli 'user' z indeksu ule
    taki indeks trzeba dopiero stworzyć
    lista ule zawiera indeksy uli przypisane do id użytkownika
    '''
    ule = [1,2]
    return ule

def check_err(id):  #to chcę na zaraz
    '''
    sprawdza ostatni stan stan ula dla jego id z tabeli alerty, 
    jesli nie ma erroru zwraca w ciagu ostatnich 5 minut daje False
    '''
    if id == 1:
        return False, 'good'
    if id == 0:
        return True, 'bad: error type'

def get_err(id):
    '''
    zwraca ostatnie 10 errorów dla dane id ula
    '''
    tab = [['2020-01-17; 18:48:09','E01', 'Ziąb'], ['2020-01-17; 18:48:09','E02', 'Miód'], 
    ['2020-01-17; 18:48:09','E00', 'Nieznany błąd'], 
    ['2020-01-17; 18:48:09','E01', 'Ziąb'], ['2020-01-17; 18:48:09','E03', 'Ucieczka']]
    return tab

def get_inf(id): #to chcę na zaraz
    '''
    ważna funkcja służy do pobierania informacji o aktualnych właściwościach ula o danym id
    '''
    data, temp, waga, humi = '2020-01-17 18:48:09', '23.2', '6.4', '68'
    return data, temp, waga, humi

def get_all(id, date):
    '''
    przyszlosciowa funkcja
    zwraca listę dwuwymiarową z danymi od danej daty do dnia dzisiejszego
    '''
    tab = [['77112020-01-17; 18:48:09; 24; 54; 0'   ],
    ['77212020-01-17; 18:48:14; 23.2; 55; 0'   ],
    ['77312020-01-17; 18:48:19; 23.8; 59; 0'   ],
    ['77412020-01-17; 18:48:24; 23.8; 56; 0'   ],
    ['77512020-01-17; 18:48:29; 23.9; 54; 0'   ],
    ['77612020-01-17; 18:48:34; 23.2; 54; 0'   ]]
    return tab
