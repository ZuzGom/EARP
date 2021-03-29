from datetime import datetime, timedelta
from mysql.connector import connect, Error

def polaczenie():
    try:
        connection = connect(
            host="ekonomik.atthost24.pl",
            user="18013_earp",
            password="earp.123",
            database="18013_earp"
        )
        return connection
    except Error as e:
        notification.notify(title=e, message=e[50:])



def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        result = '0'
        return result


#ważna funkcja służy do pobierania informacji o aktualnych właściwościach ula
def get_inf():
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT temperature, AdditionalTemperature, Weight, Humidity, Date, Time FROM Measurements"
        query = execute_read_query(connection, select_query)[-1]

        #temperatura wewnetrzna - temp1
        temp1 = str(query[0])

        #temperatura zewnetrzna - temp2
        temp2 = str(query[1])

        #obliczanie wag
        waga_all_string = str(query[2])
        waga1=waga_all_string[0]
        waga2=waga_all_string[1:3]
        waga = waga1 + '.' + waga2

        humi = str(query[3])
        kalendarz = str(query[4])
        zegar = str(query[5])

        data = kalendarz + "\n" + zegar
        temp= "zew: "+ temp1 + '°C\nwew: ' +temp2 + '°C'

        connection.disconnect()
        return data, temp, waga + 'kg', humi + '%'

    else:
        temp='zew: 0°C\nwew: 0°C'
        waga='0'
        humi='0'
        data = "00-00-0000 \n 00:00:00"

        return data, temp, waga + 'kg', humi + "%"

get_inf()

#funkcja dla Zuzi, sprawdza czy sie updatuje
def data():
    now = datetime.now()
    return str(now)


#przyszlosciowa funkcja
#zwraca listę dwuwymiarową z danymi od danej daty do obecnego czasu
def get_all(id, time):
   
    date = datetime.now()-timedelta(minutes=time)
    #od tej daty ^ 

    #licza sie dla mnie trzy ostatnie indeksy
    #data, godzina, temp_zew, temp_wew, wilgotnosc, waga
    tab = [
    ['77112020-01-17',' 18:48:09',' 2','4',' 54',' 0'],
    ['77212020-01-17',' 18:48:14',' 23','2',' 55',' 0'],
    ['77312020-01-17',' 18:48:19',' 23','8',' 59',' 0'],
    ['77412020-01-17',' 18:48:24',' 23','8',' 56',' 0'],
    ['77512020-01-17',' 18:48:29',' 23','9',' 54',' 0'],
    ['77612020-01-17',' 18:48:34',' 23','2',' 54',' 0']
    ]
    return tab

def get_all_day():
    teraz = datetime.now()
    dzien = str(teraz.day)
    miesiac = str(teraz.month)
    rok = str(teraz.year)

    tab = []

    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Day, Month, Year, Hour, Minute, Second, Temperature, AdditionalTemperature, Humidity, Weight FROM Measurements WHERE Day = " + dzien + " AND Month = " + miesiac + " AND YEAR = " + rok
        query = execute_read_query(connection, select_query)

        tab.append(query)

    connection.disconnect()
    return tab


'''
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
    

                                                                                                        #to chcę na zaraz
def check_err(id):
    
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