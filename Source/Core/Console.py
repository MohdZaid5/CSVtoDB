
"""
This file contains ABC( abstract base class ) for console object with some defining properties stored in dataclasses.
"""

__version__ = 1
__author__  = 'Mohd Zaid'

# Local imports
from Frontend.Color import Colors, Colored

# Inbuilt
from datetime import datetime
from dataclasses import dataclass

import os

from typing import Callable, Any
# foo = lambda *args, **kwargs : None is used as callable

@dataclass
class Logging:

    '''
    Used for logging processes.
    `FOLDER_PATH`   : Absolute or relative but path
    `FILE_NAME`     : Name of file with `extension` included init.

    `MAX_BYTE_SIZE` : If exceeded file is reset to no `bytes` stored to improve performance `$Not in use` rn.
    '''

    # Basic requirements
    FOLDER_PATH: str    # Absolute or reletive but path.
    FILE_NAME  : str    # Name of file with extension included init.

    # Handle
    MAX_BYTE_SIZE: int  =  0   # If exceeded file is reset to no bytes stored to improve performance $Not in use rn.

    # Problem can arise if folder is not present so creating folder.
    def failsafe( self ):
        if not os.path.exists( self.FOLDER_PATH ): os.makedirs( self.FOLDER_PATH )
        return self

    def __call__(self, text:str):
        
        '''This logs provided `text` to file.'''

        with open( os.path.join( self.FOLDER_PATH, self.FILE_NAME), 'a') as LogFile:
            LogFile.write(f"{text}\n")


@dataclass
class ConsoleObj:

    '''
    This function can be used as basic build for any console object
    `BACKGROUND`: Background `Color` of alias.
    `FOREGROUND`: Foreground `Color` of alias.
    `HIGHLIGHTS`: Highlight  `Color` of alias.
    `ALIAS_NAME`: `Text` over the alias.
    `SHOW_TIME `: If `time` is to be shown next to console.
    `CONSOLEOUT`: If output is to be shown in `console`.
    `LOG_TO_FIL`: If to be `logged`.
    `FILE_NAME `: Name of log file.
    `FOLDERNAME`: Name of folder in which it is to be logged
    `LOGGING_OBJ`: just a logging object.
    `SPECIAL_BEHAVIOURS`: allows to add function in `__call__` to help better the behaviors.

    *`!` `@SPECIAL_BEHAVOIUR` Disables `CONSOLEOUT` and `LOG_TO_FIL` automatically.*
    '''

    # Some Basic Properties.
    BACKGROUND: Colors  # Background `Color` of alias.
    FOREGROUND: Colors  # Foreground `Color` of alias.
    HIGHLIGHTS: Colors  # Highlight  `Color` of alias.
    ALIAS_NAME: str     # Text over the alias.

    # Some Basic Behaviours
    SHOW_TIME : bool  =  False  # If `time` is to be shown next to console.
    CONSOLEOUT: bool  =  False  # If output is to be shown in `console`.

    # Log File Properties
    LOG_TO_FIL: bool  =  False          # If to be `logged`.
    FILE_NAME : str   =  'Main.log'     # Name of log file.
    FOLDERNAME: str   =  'Logs'         # Name of folder in which it is to be logged
    
    # Other objects, varieables and utilities.
    SPECIAL_BEHAVIOURS: bool      = False   # Gives Special behaviout to `__call__`
    OUTPUT_BEHAVIOUR  : Callable  = Callable
    CURSOR_OBJECT     : Callable  = None    # Removed feature

    @property
    def LOGGING_OBJ( self ):
        return Logging( self.FOLDERNAME ,self.FILE_NAME ).failsafe()

    @property
    def Alias( self ): # Initialises alias and puts it together.
        return Colored.console(f"[{self.ALIAS_NAME.center(13)}]", self.FOREGROUND, self.BACKGROUND)
    
    @property
    def Time( self ): # If time is to be shown, gets and colors the time part.
        return Colored.text( str( datetime.now().time() ).split('.')[0], Colors.GRAY15 )
    
    def __call__(self, *parts:str, sep:str=' ', end:str='\n', console_out:bool=False):

        '''
        As per requirements this can handle  [`ConsoleOutput`, `LogHandling`].
        
        arguments
        `*parts`        : Are part of `sentence` or `para` that is to be printed
        
        keyword arguments
        `sep`           : `part` seperation `str`
        `end`           : The `str` that is to be placed at end.
        '''

        if self.SPECIAL_BEHAVIOURS: self.LOG_TO_FIL = self.CONSOLEOUT = False

        assembled = []

        # Highlighting process.
        for part in parts: 
            if '*' in part: assembled.append( Colored.text( part.replace('*',''), self.HIGHLIGHTS ) )
            else: assembled.append( part )
        
        # Joining highlighted and non highlighted parts.
        sentence = f'{sep}'.join( assembled )

        # Output on console.
        if self.CONSOLEOUT or console_out:
            if self.SHOW_TIME: print( f'{self.Alias}  {self.Time}  {sentence}', end=end)
            else: print( f'{self.Alias}  {sentence}', end=end)

        # Logging process.
        if self.LOG_TO_FIL:
            self.LOGGING_OBJ( f"[{self.ALIAS_NAME.center(13)}]  {str(datetime.now().time()).split('.')[0]}  {f'{sep}'.join(parts)}" )

        # Use of special behaviour function.
        if self.SPECIAL_BEHAVIOURS:
            if self.SHOW_TIME: return self.OUTPUT_BEHAVIOUR( text = f'{self.Alias}  {self.Time}  {sentence}' )
            else: return self.OUTPUT_BEHAVIOUR( text = f'{self.Alias}  {sentence}' )


@dataclass
class Progress:

    """
    This class Deals with showing progress bar.
    `MAX`       : Maximum value of items
    `MIN`       : Minimum value of items
    `VAL`       : Current value of items
    `Console`   : Console object.
    """

    # Basic values
    MAX : int 
    MIN : int
    VAL : int

    # Behaviors
    CONSOLE : ConsoleObj | Callable

    def __add__( self, value:int ):

        """
        Adding To progress
        """

        self.VAL += value
        prcnt = int((self.VAL/self.MAX)*100)
        self.__call__( 'Converting', f'*|{"#"*(prcnt)}{("-"*(100-prcnt))}|', end='\r')

        if self.VAL == self.MAX:
            self.__call__( 'Converting', f'*|{"#"*(prcnt)}{("-"*(100-prcnt))}|')


    def __call__(self, *args: Any, end='\n') -> Any:
        
        self.CONSOLE( *args, end=end)