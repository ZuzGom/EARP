from datetime import datetime, timedelta
from mysql.connector import connect, Error
import requests
from bs4 import BeautifulSoup

#Function for Zuzia, check if the time is updatet
def data():
    now = datetime.now()
    return str(now)

# funkcja która zwraca URL bazy
def tcp():
    try:
        page = requests.get('https://github.com/ZuzGom/remote/blob/main/tcp.txt')
    except requests.exceptions.ConnectionError:
        linia = "None:None:None"
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')
        linia = str(soup.find("td", {"id": "LC1"})).split()[-1][9:-5]                        
    return linia

def track():
    try:
        page = requests.get('https://github.com/ZuzGom/remote/blob/main/url.txt')
    except requests.exceptions.ConnectionError:
        linia = "None:None:None"
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')
        linia = str(soup.find("td", {"id": "LC1"})).split()[-1][9:-5]                        
    return linia

#Function which connect with database
def polaczenie():
    u_tcp = tcp().split(':')
    host=u_tcp[1][2:]
    port=u_tcp[2]
    try:
        connection = connect(
            host=host,
            port=port,
            user="ul",
            password="earp123",
            database="Dane"
        )
        return connection
    except Error as e:
        print(e)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        result = None
        return result

#Function which gives data to database
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print("The error " + str(e) + " occurred")

#Important function, which download live information about bees house
def get_inf():
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Temperature, AdditionalTemperature, Humidity, Weight, Date, Time, Year, Month, Day, Hour, Minute, Second FROM Measurements ORDER BY Datetime DESC LIMIT 1"
        query = execute_read_query(connection, select_query)[0]

        connection.close()

        #Temperature inside - temp1
        temp1 = str(query[0])

        #Temperature outside - temp2
        temp2 = str(query[1])

        humi = str(query[2])
            
        #Zuzia solution - Waga
        waga = str(int(float(query[3]))/1000)
        
        kalendarz = str(query[4])
        zegar = str(query[5])
        
        #Musisz sobie jakos zrobic tego tuple bo ja chyba nie czaje

        data = kalendarz + "\n" + zegar
        temp= "zew: "+ temp1 + '°C\nwew: ' + temp2 + '°C'

        return data, temp, waga + 'kg', humi + '%'

    else:
        temp='zew: 0°C\nwew: 0°C'
        waga='0'
        humi='0'
        data = "00-00-0000 \n 00:00:00"

        return data, temp, waga + 'kg', humi + "%"

#Function return 'tab[]' to TODAY graph
def get_all_day():
    teraz = datetime.now()
    dzien = str(teraz.day)
    miesiac = str(teraz.month)
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Temperature, AdditionalTemperature, Humidity, Weight, Date, Time, Year, Month, Day, Hour, Minute, Second FROM Measurements WHERE (Day = " + dzien + " AND Month = " + miesiac + " AND Year = " + rok + ") ORDER BY Datetime DESC"
        query = execute_read_query(connection, select_query)
        connection.close()

        for x in query: 
            line = [x[-6:]]
            line += list(x[:4])
            line[-1]=int(float(line[-1]))/1000
            tab.append(line)

    return tab

#Function return 'tab[]' to hour back graph
def get_all_hour():
    teraz = datetime.now()
    minuta = str(teraz.minute)
    godzina = str(teraz.hour)
    dzien = str(teraz.day)
    miesiac = str(teraz.month)
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Temperature, AdditionalTemperature, Humidity, Weight, Date, Time, Year, Month, Day, Hour, Minute, Second FROM Measurements WHERE ( Year = " + rok + " AND Month = " + miesiac + " AND Day = " + dzien + " AND  Hour = " + godzina + " AND Minute <= " + minuta + " ) OR ( Year = " + rok + " AND Month = " + miesiac + " AND Day = " + dzien + " AND HOUR = " + godzina + " AND Minute >= " + minuta + " ) ORDER BY Datetime DESC"
        query = execute_read_query(connection, select_query)
        connection.close()

        for x in query:
            line = [x[-6:]]
            line += list(x[:4])
            line[-1]=int(float(line[-1]))/1000
            tab.append(line)

    return tab

print(get_all_hour())

#Function return 'tab[]' to month back graph
def get_all_month():
    teraz = datetime.now()
    dzien = str(teraz.day)
    miesiac = str(teraz.month)
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Temperature, AdditionalTemperature, Humidity, Weight, Date, Time, Year, Month, Day, Hour, Minute, Second FROM Measurements WHERE (Day <= " + dzien + " AND Month = " + miesiac + " AND Year = " + rok + " ) OR ( Day >= " + dzien + " AND Month = " + str(int(miesiac)-1) + " AND Year = " + rok + ") ORDER BY Datetime DESC"
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = [x[-6:]]
            line += list(x[:4])
            line[-1]=int(float(line[-1]))/1000
            tab.append(line)
        
            
    return tab

#Function return 'tab[]' since begin of the year 
def get_all_year():
    teraz = datetime.now()
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Temperature, AdditionalTemperature, Humidity, Weight, Date, Time, Year, Month, Day, Hour, Minute, Second FROM Measurements WHERE Year = " + rok + " ORDER BY Datetime DESC"
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = [x[-6:]]
            line += list(x[:4])
            line[-1]=int(float(line[-1]))/1000
            tab.append(line)

    return tab

#return tables with data included from now to some date
def get_all(rok, miesiac, dzien):
    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Temperature, AdditionalTemperature, Humidity, Weight, Water, Sound, AccelerationX, AccelerationY, AccelerationZ, RotationX, RotationY, RotationZ, Date, Time, Year, Month, Day, Hour, Minute, Second FROM Measurements WHERE ( Year = " + str(rok) + " AND Month = " + str(miesiac) + " AND Day >= " + str(dzien) + ") OR ( Year = " + str(rok) + " AND Month > " + str(miesiac) + ") OR ( Year > " + str(rok) + " )"
        query = execute_read_query(connection, select_query)
    
        for x in query:
            line = [x[-6:]]
            line += list(x[:12])
            tab.append(line)
    
    return tab

#Function pushing alert
def push_alert(id, error, tresc):
    connection = polaczenie()
    
    if(connection!=None):
        inserting_error = "INSERT INTO Alerty ( id, error, tekst ) VALUES ( " + str(id) + ", " + str(error) + ", \"" + tresc + "\" )"
        execute_query(connection, inserting_error)
    
    connection.close()
    
#Function return 'tab[]' with last 5 records from table - Alerty
def get_err():
    connection = polaczenie()
    tab = []
    
    if(connection!=None):
        select_query = "SELECT * FROM Alerty WHERE id>=0 ORDER BY data DESC LIMIT 5"
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = x
            tab.append(line)
    
    return tab

'''
#Future function
def get_ule(id):
    
    ta przyszłościowa funkcja służy do pobierania informacji z tabli 'user' z indeksu ule
    taki indeks trzeba dopiero stworzyć
    lista ule zawiera indeksy uli przypisane do id użytkownika
    
    ule = [1,2]
    return ule
    
'''