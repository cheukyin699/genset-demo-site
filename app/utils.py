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

# Functions
def sid_is_valid(sid):
    '''
    Checks to see if the session ID is valid or not. Valid session IDs do not
    contain slashes of any kind, and should not attempt to do any directory
    traversal.
    '''
    return not '/' in sid and not '\\' in sid and not '.' in sid and sid in VALID_TEMPS
