'''
The utilities module

This module is a collection of useful functions and tidbits that come in handy
for some things. It contain functions that may be too big to be inlined, but
too small to deserve a module of their own. It also contains global variables
and global constants that are used in other parts of the website.

The goal of this module is simple: to abstract out as much code as possible from
the main files, so that one could focus more on the logic, and less of the code.
'''
from tempfile import mkdtemp
from os.path import basename

# Variables
SAMPLE_FILES = [
    ('E. coli', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/E_Coli_Training.csv'),
    ('S. dysenteriae', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/S_Dysenterae_Training.csv'),
    ('S. typhimurium', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/S_Typhimurium_Training.csv'),
    ('P. syringae', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/P_Syringae_Training.csv'),
    ('X. campestris', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/X_Campestris_Training.csv'),
    ('C. trachematis', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/C_Trachomatis_Training.csv'),
    ('E. coli + S. dysenteriae', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/E_Coli_S_Dysenteriae_Training.csv'),
    ('E. coli + S. dysenteriae + S. typhimurium', 'https://raw.githubusercontent.com/cheukyin699/genset-training-csvs/master/E_Coli_S_Dysenteriae_S_Typhimur_Training.csv'),
]

VALID_TEMPS = []

FILE_MAP = {
    'ecoli': 'E_Coli_Training.csv',
    'spi1': 'S_Dysenterae_Training.csv',
    'spi2': 'S_Typhimurium_Training.csv',
    'hrp1': 'P_Syringae_Training.csv',
    'hrp2': 'X_Campestris_Training.csv',
    'chl': 'C_Trachomatis_Training.csv',
}

# Functions
def sid_is_valid(sid):
    '''
    Checks to see if the session ID is valid or not. Valid session IDs do not
    contain slashes of any kind, and should not attempt to do any directory
    traversal.
    '''
    return not '/' in sid and not '\\' in sid and not '.' in sid and sid in VALID_TEMPS

def create_temp_folder(d):
    '''
    Creates a temporary folder in directory `d`. Returns the path and name of
    the temporary folder (commonly known as session ID) in tuple form. Appends
    the session ID to the list of valid sessions `VALID_TEMPS`.
    '''
    path = mkdtemp(dir=d, prefix='')
    session_id = basename(path)
    VALID_TEMPS.append(session_id)

    return path, session_id
