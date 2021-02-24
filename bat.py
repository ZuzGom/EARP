from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="18013_earp",
        user="18013_earp",
        password=getpass("earp.123"),
    ) as connection:
        print(connection)
except Error as e:
    print(e)