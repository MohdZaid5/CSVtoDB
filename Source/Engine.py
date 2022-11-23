
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


# Navigation for program
def menu():

    # Making all local varibales into global
    global db_type
    global cursor
    global connection
    global csv_file
    global csv_file_path
    global db_table_name
    
    # Asking if user want to add that entry into mysql.db or sqlite.
    options_1 = [
    '\nWhere do you want to make entry:',
    '*   [f] -  To a "db" file using sqlite.',
    '*   [d] -  To a existing "db" in system. <feature-not-implimented>\n']
    db_type= Console.Input(*options_1, sep='\n')
    Console.Log('To the question "where do you want to ..." user entered',f'*{db_type}')

    # making connection and cursor
    if 'd' in db_type.lower():
        Console.Error('This feature is','*[Not]','yet present.')
        Console.Log('Explicitly selecting', '[f]', 'as choice')
        db_type = 'f'
    if 'f' in db_type.lower():
        # Gathering informations.
        csv_file_path= Console.Input('Provide path to','*[csv]','file')
        db_file_name = Console.Input('Provide name with which','*[db]','file is to be saved')
        db_table_name= Console.Input('Provide name of table inside','*[db]','where data is to be saved')
        # Checking informations
        # Database directory
        if not os.path.exists('Database'):
            os.makedirs('Database')
        # Processing to transfer data
        connection = sqlite3.connect(f'Database\\{db_file_name}.db')
        cursor     = connection.cursor()
    else:
        Console.Log(f'*{db_type=}', 'Not able to perform anything.','*No such command')
        menu()

menu()

# If provided csv exists
if not os.path.exists(csv_file_path): Console.Error('File',f'*{csv_file_path}','Does not exists.')


# All commands
CREATE_TABLE = \
'''
CREATE TABLE IF NOT EXISTS {} (
        {}
);
'''
COLUMNS = 'VARCHAR,\n\t'
INSERT_INT = \
'''
INSERT INTO {}
VALUES ("{}")
'''
VALUES = '","'


# Convertor
with open( csv_file_path, 'r' ) as csv_file:
    file_data = csv.reader( csv_file )

    for index, data in enumerate(file_data):
        try:
            if index == 0: cursor.execute( CREATE_TABLE.format( db_table_name, COLUMNS.join(data)) ); continue
            cursor.execute( INSERT_INT.format( db_table_name, VALUES.join(data) )) 
        except Exception as Exc:
            Console.Error(f"{Exc}*")
    
    connection.commit()

SQL.output('Sucessfully Converted','*[csv]','data to','*[db] entry.')

# End
input()
quit()

# Code blelow will not be executed as program is ended at line <97>
# Possible implimentation of 'd'

#if 'd' in db_type.lower():
#    # Gathering informations
#    csv_file_path:str = Console.Input('Provide path to','*[csv]','file')
#    db_passwd   :str  = Console.Input('Enter your local','*mySql Password')
#    db_name     :str  = Console.Input('Provide name in which','*[db]','database info is to be saved')
#    db_table_name:str = Console.Input('Provide name of table inside','*[db]','where data is to be saved')
#    # Creating cursor
#    try:
#        connection = mysql.connector.connect(host='localhost',passwd=db_passwd,database=db_name)
#        cusrsor = connection.cursor()
#    except NameError:
#        Console.Error('Failed to establish connection', '*As mysql.connector is not properly installed.')
#        
#        Console.Log('Using sqlite')
#        connection = sqlite3.connect(f'Database\\{db_name}.db')
#        cursor     = connection.cursor()
#
#    except Exception as Exc:
#        Console.Error('Failed to fetch cursor as',f"*{Exc}")
#        
#        Console.Log('Using sqlite')
#        connection = sqlite3.connect(f'Database\\{db_name}.db')
#        cursor     = connection.cursor()
