
"""
This program converts csv entries into database entries.
    -   User can choose to use server database or file `.db`.
"""

# Info
__version__ = 1
__author__  = 'Mohd Zaid'

# Imports from other files.
from Frontend.Stylers import Console, SQL, process_out
from Core.Console import Progress

# Imports from inbulit library.
from dataclasses import dataclass
from typing import Any
import csv
import os
import sqlite3

#Dependent Imports
# If mysql.connector (python) is not installed.
# Download - python pip install mysql-connector-python
try:
    import mysql.connector
    Console.Log('Imported mysql.connector')
except ModuleNotFoundError as MNFErr:
    Console.Error('Encountered error while trying to import','*mysql.connector')
    Console.Log('Error while importing','*mysql.connector',f'{MNFErr}')
    Console.Log('To install connector run command','*python pip install mysql-connector-python')
# This feature may be added to [__version__ = 2] of this program


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


# Menu
@dataclass
class Menu_Result:

    db_type : str
    cursor  : sqlite3.Connection
    connenction : sqlite3.Connection
    file_path : str
    db_table_name : str

class Menu:

    # Navigation for program
    @staticmethod
    def Terminal_menu(  ) -> Menu_Result :
        
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
            file_path= Console.Input('Provide path to','*[csv]','file')
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
            return Menu.Terminal_menu()
        
        # If provided csv exists
        if not os.path.exists(file_path): Console.Error('File',f'*{file_path}','Does not exists.'); return Menu.Terminal_menu()

        return Menu_Result( db_type, cursor, connection, file_path, db_table_name )


# Engines
class Engine:

    @staticmethod
    def CSVtoDB( csv_file_path, db_table_name, cursor, connection ):
        # Convertor
        with open( csv_file_path, 'r' ) as csv_file:
            file_data = csv.reader( csv_file )

            progress = Progress( len(file_data), 0, 0, process_out )
            for index, data in enumerate(file_data):
                try:
                    if index == 0: cursor.execute( CREATE_TABLE.format( db_table_name, COLUMNS.join(data)) ); continue
                    cursor.execute( INSERT_INT.format( db_table_name, VALUES.join(data) )) 
                except Exception as Exc:
                    Console.Error(f"{Exc}*")
                progress + 1
            
            connection.commit()
            return True
    
    @staticmethod
    def XLStoDB( xls_file_path, db_table_name, cursor, connection ):
        ...