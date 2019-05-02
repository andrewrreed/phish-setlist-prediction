'''
Utility functions for the pyphish package

'''
import os
import pickle
from bs4 import BeautifulSoup



def create_pickle_object(obj, pickle_name, file_path='./pickle_objects/'):
    """Pickle a Python object and save to local directory

    Parameters
    ----------
    obj : Python object
        The Python object to pickle
    pickle_name : string
        The file name of that will be saved with the file; must end with '.pickle' suffix
    file_path : string
        The path (absolute or relative) to the target directory where the pickle file will be stored
    """

    # validate datatypes
    if isinstance(pickle_name, str) and isinstance(file_path, str):

        # verify .pickle suffix
        if pickle_name[-7:] != '.pickle':
            raise ValueError('The pickle_name argument must end with a .pickle suffix.')

        # build full path
        full_path = file_path + pickle_name
    else:
        raise ValueError('Both file_name and file_path arguments must be of type string.')

    # check if directory exists - create if it doesnt
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # open new file and dump serialized data
    pickle_out = open(full_path, 'wb')
    pickle.dump(obj, pickle_out)
    pickle_out.close()

    print(f'Successfully pickled {obj} to {os.path.abspath(full_path)}')

    return None

def load_pickle_object(file_path):
    """Load a pickled Python object from local directory

    Parameters
    ----------
    file_path : string
        The path (absolute or relative) to the target directory where the pickle file is stored

    Returns
    -------
    pickle_obj : Python object
        The Python object from stored serialized representation
    """

    # check if file_path is string
    if not isinstance(file_path, str):
        raise TypeError('The file_path argument must be a string.')

    # check if the file exists
    if not os.path.exists(file_path):
        raise NameError('The file or path provided does not exist.')

    # verify .pickle file as target
    if file_path[-7:] != '.pickle':
        raise ValueError('The file must end with a .pickle suffix.')

    pickle_in = open(file_path, 'rb')
    pickle_obj = pickle.load(pickle_in)

    return pickle_obj
