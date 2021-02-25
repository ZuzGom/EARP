from getpass import getpass
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