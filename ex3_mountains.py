def read_the_file(file):
    """
    Returns the data of the file file
    :param file: the file to read (str)
    :return: the data (dictionnary)
    """

    fh = open(file, 'r')
    lines = fh.readlines()
    dico = {}
    for line in lines:
        elements = line.split(';')
        dico[elements[0].strip()] = (elements[1].strip(), elements[2].strip())

    fh.close()
    return dico


print(read_the_file('mountains.txt'))
