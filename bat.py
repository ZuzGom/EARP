from getpass import getpass
from mysql.connector import connect, Error

try:
    print('lets go')
    with connect(
        host="ekonomik.atthost24.pl",
        name="18013_earp",
        user="18013_earp",
        password=getpass("earp.123"),
    ) as connection:
        print('bro')
        print(connection)
except Error as e:
    print(e)
print('no')