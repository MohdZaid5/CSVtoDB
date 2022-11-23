
"""
This program converts csv entries into database entries.
    -   User can choose to use server database or file `.db`.
"""

# Info
__version__ = 1
__author__  = 'Mohd Zaid'

# Imports from other files.
from Frontend.Stylers import Console, SQL

# Imports from inbulit library.
import csv
import os
import sqlite3

#Dependent Imports
# If mysql.conncetor (python) is not installed.
# Download - python pip install mysql-connector-python
try:
    import mysql.connector
    Console.Log('Imported mysql.connector')
except ModuleNotFoundError as MNFErr:
    Console.Error('Encountered error while trying to import','*mysql.connector')
    Console.Log('Error while importing','*mysql.connector',f'{MNFErr}')
    Console.Log('To install connector run command','*python pip install mysql-connector-python')
# This feature may be added to [__version__ = 2] of this program


# Database Directory
if not os.path.exists('.\Database'):
    os.makedirs('.\Database')

db = Console.Input('Enter database name')

# Sqlite3 Connection
# mySql connection feature-not-present
connection = sqlite3.connect( f'Database\\{db}.db' )
cursor = connection.cursor()

# Header
SQL.output( '*Enter Sql Code for querry below', 'this is operatied in while loop')
Console.Log( 'Press',"[ctrl] + [c]", 'to exit')

# Main program
while True:
    try:
        SQL.output('x-'*30,'x', sep='')
        Command = SQL.input()
        cursor.execute(Command)

        result = cursor.fetchall()
        for res in result:
            SQL.output(f'*{res}')
    except KeyboardInterrupt:
        Console.Log('*Exiting','Programme')
        break
    except Exception as Exc:
        Console.Error('*Encountered an Error', f'*{Exc}')
    else:
        connection.commit()

connection.close()

# End
input()
quit()