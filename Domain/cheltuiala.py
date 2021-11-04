def create_cheltuiala(id, numar_apartament, suma, data, tipul):
    '''

    :param id: string
    :param numar_apartament: int
    :param suma: float
    :param data: string
    :param tipul: string
    :return: Dict
    '''


    return{
        "id": id,
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tipul": tipul
    }

def get_id(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: id - string
    '''
    return cheltuiala['id']

def get_numar_apartament(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: numar_apartament - int
    '''
    return cheltuiala['numar_apartament']

def get_suma(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: suma - float
    '''
    return cheltuiala['suma']

def get_data(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: data - string
    '''
    return cheltuiala['data']

def get_tipul(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: tipul - string
    '''
    return cheltuiala['tipul']

def to_str(cheltuiala):
    return f'id={get_id(cheltuiala)}, numar_apartament={get_numar_apartament(cheltuiala)}, suma={get_suma(cheltuiala)}'\
            f'data={get_data(cheltuiala)}, tip={get_tipul(cheltuiala)}'

