from datetime import datetime, timedelta
from mysql.connector import connect, Error

#Function which connect with database
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
        return notification.notify(title=e, message=e[50:])


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error:
        result = None
        return result


#Function which gives data to database
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        #print("Query executed successfully")
    except Error as e:
        #print("The error " + str(e) + " occurred")


#Important function, which download live information about bees house
def get_inf():
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT temperature, AdditionalTemperature, Weight, Humidity, Date, Time FROM Measurements"
        query = execute_read_query(connection, select_query)[-1]

        connection.close()

        #Temperature inside - temp1
        temp1 = str(query[0])

        #Temperature outside - temp2
        temp2 = str(query[1])

        #Zuzia solution
        waga = str(int(float(query[2]))/1000)

        humi = str(query[3])
        kalendarz = str(query[4])
        zegar = str(query[5])

        data = kalendarz + "\n" + zegar
        temp= "zew: "+ temp1 + '°C\nwew: ' + temp2 + '°C'

        return data, temp, waga + 'kg', humi + '%'

    else:
        temp='zew: 0°C\nwew: 0°C'
        waga='0'
        humi='0'
        data = "00-00-0000 \n 00:00:00"

        return data, temp, waga + 'kg', humi + "%"


#Function for Zuzia, check if the time is updatet
def data():
    now = datetime.now()
    return str(now)


#ale batiś to jest projekt dla polskich pszczelarzy
#chyba że lubisz sobie utrudniać ;)
#Kiedyś do CV będzie można sobie wrzucić i lepiej będzie wyglądały komentarze po angielsku


#Future function
#return 2D tables with data included from now to some date
def get_all(dni):
    date = datetime.now()-timedelta(minutes=dni)
            #od tej daty

    #data, godzina, temp_wew, temp_zew, wilgotnosc, waga
    tab = [
    ['77112020-01-17',' 18:48:09',' 22','24',' 54',' 0'],
    ['77212020-01-17',' 18:48:14',' 23','22',' 55',' 0'],
    ['77312020-01-17',' 18:48:19',' 23','28',' 59',' 0'],
    ['77412020-01-17',' 18:48:24',' 23','28',' 56',' 0'],
    ['77512020-01-17',' 18:48:29',' 23','29',' 54',' 0'],
    ['77612020-01-17',' 18:48:34',' 23','22',' 54',' 0']
    ]
    return tab


#Function return 'tab[]' to TODAY graph
def get_all_day():
    teraz = datetime.now()
    dzien = str(teraz.day)
    miesiac = str(teraz.month)
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Day, Month, Year, Hour, Minute, Temperature, AdditionalTemperature, Humidity, Weight FROM Measurements WHERE Day = " + dzien + " AND Month = " + miesiac + " AND Year = " + rok
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = [(x[:3]),(x[3:5])] + list(x[5:])
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
        select_query = "SELECT Day, Month, Year, Hour, Minute, Temperature, AdditionalTemperature, Humidity, Weight FROM Measurements WHERE ((Hour=" + str(int(godzina)-1) + " AND Minute<=" + minuta + " ) AND Day=" + dzien + " AND Month = " + miesiac + " AND Year = " + rok + ") OR (( Hour = " + str(int(godzina)-2) + " AND Minute >= " + minuta + " ) AND Day = " + dzien + " AND Month = " + miesiac + " AND Year = " + rok + ")"
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = [(x[:3]), (x[3:5])] + list(x[5:])
            line[-1] = int(float(line[-1])) / 1000
            tab.append(line)

    return tab


#Function return 'tab[]' to month back graph
def get_all_month():
    teraz = datetime.now()
    dzien = str(teraz.day)
    miesiac = str(teraz.month)
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Day, Month, Year, Hour, Minute, Temperature, AdditionalTemperature, Humidity, Weight FROM Measurements WHERE (Day <= " + dzien + " AND Month = " + miesiac + " AND Year = " + rok + " ) OR ( Day >= " + dzien + " AND Month = " + str(int(miesiac)-1) + " AND Year = " + rok + ")"
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = [(x[:3]), (x[3:5])] + list(x[5:])
            line[-1] = int(float(line[-1])) / 1000
            tab.append(line)
            
    return tab


#Function return 'tab[]' since begin of the year 
def get_all_year():
    teraz = datetime.now()
    rok = str(teraz.year)

    tab = []
    connection = polaczenie()

    if(connection!=None):
        select_query = "SELECT Day, Month, Year, Hour, Minute, Temperature, AdditionalTemperature, Humidity, Weight FROM Measurements WHERE Year = " + rok
        query = execute_read_query(connection, select_query)

        connection.close()

        for x in query:
            line = [(x[:3]), (x[3:5])] + list(x[5:])
            line[-1] = int(float(line[-1])) / 1000
            tab.append(line)

    return tab


#Function works
def push_alert(id, error, tresc):

    connection = polaczenie()
    
    if(connection!=None):
        inserting_error = "INSERT INTO Alerty ( id, error, tekst ) VALUES ( " + str(id) + ", " + str(error) + ", \"" + tresc + "\" )"
        execute_query(connection, inserting_error)
    
    connection.close()
    
push_alert(15, 6, "Test godziny")

#Nie robilem nic przy niej
def get_err():
    #zwraca ostatnie 5 linii z tabeli Alerty
    
    tab = [['2020-01-17; 18:48:09','1','1' ,'Ziąb'], ['2020-01-17; 18:48:09','1','2' , 'Miód'], 
    ['2020-01-17; 18:48:09','8','1' , 'Nieznany błąd'], 
    ['2020-01-17; 18:48:09','1','1' , 'Ziąb'], ['2020-01-17; 18:48:09','1','3' , 'Ucieczka']]
    return tab


'''
def get_ule(id):
    
    ta przyszłościowa funkcja służy do pobierania informacji z tabli 'user' z indeksu ule
    taki indeks trzeba dopiero stworzyć
    lista ule zawiera indeksy uli przypisane do id użytkownika
    
    ule = [1,2]
    return ule

'''