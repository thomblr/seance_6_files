import pickle
import os

# Initialize the file
if not os.path.exists('codedata_structure.pkl'):
    list_of_data = [('nom', 'R2D2'), ('age', 42), ('prenom', 'Z-6PO')]
    fh = open('codedata_structure.pkl', 'wb')
    pickle.dump(list_of_data, fh)
    fh.close()


# Read the file (1st function)
def read_the_file(file):
    """
    Returns the data of the file file
    :param file: the file (str)
    :return: the data (list)
    """

    fg = open(file, 'rb')
    values = pickle.load(fg)
    fg.close()
    return values


# Transform to dico (2nd function)
def transform_to_dico(data):
    """
    Transform the list into a dictionnary
    :param data: the list of data (list)
    :return: the dico (dictionnary)
    """

    dico = {}
    for value in data:
        dico[value[0]] = value[1]

    return dico


# Save the dictionnary in path dico/my_dico.pkl
def save_dictionnary(dictionnary):
    if not os.path.exists('dico'):
        os.mkdir('dico')

    data_file = open('dico/my_dico.pkl', 'wb')
    pickle.dump(data_file, dictionnary)
    data_file.close()

