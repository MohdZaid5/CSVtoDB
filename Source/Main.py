
"""
This program converts csv entries into database entries.
    -   User can choose to use server database or file `.db`.
"""

# Info
__version__ = 1
__author__  = 'Mohd Zaid'

# Imports from other files.
from Frontend.Stylers import Console, SQL
from Engines import Menu, Engine

# Imports from inbulit library.

#Dependent Imports
# If mysql.connector (python) is not installed.
# Download - python pip install mysql-connector-python
# This feature may be added to [__version__ = 2] of this program

info = Menu.Terminal_menu()
Engine.CSVtoDB( info.file_path, info.db_table_name, info.cursor, info.connenction )

SQL.output('Sucessfully Converted','*[csv]','data to','*[db] entry.')

# End
input()
quit()

# Code below will not be executed as program is ended at line <97>
# Possible implementation of 'd'

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
