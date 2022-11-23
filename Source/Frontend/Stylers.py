
"""
This file Contains Console / <terminal> decorator functions.
"""

__version__ = 1
__author__  = 'Mohd Zaid'


# Local imports.
from Source.Core.Console import ConsoleObj
from Source.Frontend.Color import Colored,Colors, rgb

# behavioural functions.
inp = lambda text: input( f"{text}: {Colored.raw_text( Colors.VIOLET )}" )

# Console Objects.
Log = ConsoleObj(
    BACKGROUND = Colors.GRAY, FOREGROUND = Colors.BLACK, HIGHLIGHTS = Colors.GRAY,
    ALIAS_NAME = 'Log', SHOW_TIME = True, CONSOLEOUT = True, LOG_TO_FIL = True, 
    FILE_NAME='Delveloper.log')

Error = ConsoleObj(
    BACKGROUND = Colors.CRIMSON, FOREGROUND = rgb(255,255,0), HIGHLIGHTS = Colors.RED1,
    ALIAS_NAME = 'Error', SHOW_TIME = True, CONSOLEOUT = True, LOG_TO_FIL = False # Set to true later
)

Input = ConsoleObj(
    BACKGROUND = Colors.BANANA, FOREGROUND = Colors.BLACK, HIGHLIGHTS = Colors.BANANA,
    ALIAS_NAME = 'Input', SHOW_TIME = True, CONSOLEOUT = True, LOG_TO_FIL = False, SPECIAL_BEHAVIOURS = True,
    OUTPUT_BEHAVIOUR = inp
)

# Console
class Console:
    Error   = Error
    Input   = Input
    Log     = Log

# SQL Console Object.  
sql_input = ConsoleObj(
    BACKGROUND = Colors.VIOLET, FOREGROUND = Colors.WHITE, HIGHLIGHTS = Colors.VIOLET,
    ALIAS_NAME = 'SQL', SHOW_TIME = True, CONSOLEOUT = True, LOG_TO_FIL = False, SPECIAL_BEHAVIOURS = True,
    OUTPUT_BEHAVIOUR = inp
)
            
sql_output = ConsoleObj(
    BACKGROUND = Colors.BANANA, FOREGROUND = Colors.BLACK, HIGHLIGHTS = Colors.BANANA,
    ALIAS_NAME = 'SQL', SHOW_TIME = True, CONSOLEOUT = True, LOG_TO_FIL = False
)

# Behavoural function for sql.
def sql_in( text=None ):
    command = []
    while True:
        i = sql_input('')
        command.append(i)
        if ';' in i:
            break
    return '\n'.join(command)

# SQL console
class SQL:
    input = sql_in
    output = sql_output