def create_cheltuiala(id, numar_apartament, suma, data, tipul):
    '''

    :param id: string
    :param numar_apartament: int
    :param suma: int
    :param data: string
    :param tipul: string
    :return: Dict
    '''

    # return[id, numar_apartament, suma, data, tipul]

    return {
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
    # return cheltuiala[0]
    return cheltuiala['id']


def set_id(cheltuiala, id):
    '''
    Setarea id la cheltuiala
    :param cheltuiala: Dict
    :param id: string
    :return:
    '''
    cheltuiala['id'] = id


def get_numar_apartament(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: numar_apartament - int
    '''
    # return cheltuiala[1]
    return cheltuiala['numar_apartament']


def set_numar_apartament(cheltuiala, numar_apartament):
    '''
    Setarea numar_apartament la cheltuiala
    :param cheltuiala: Dict
    :param numar_apartament: int
    :return:
    '''
    cheltuiala['numar_apartament'] = numar_apartament


def get_suma(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: suma - int
    '''
    # return cheltuiala[2]
    return cheltuiala['suma']


def set_suma(cheltuiala, suma):
    '''
    Setarea suma la cheltuiala
    :param cheltuiala: Dict
    :param suma: int
    :return:
    '''
    cheltuiala['suma'] = suma


def get_data(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: data - string
    '''
    # return cheltuiala[3]
    return cheltuiala['data']


def set_data(cheltuiala, data):
    '''
    Setarea data la prajitura
    :param cheltuiala: Dict
    :param data: string
    :return:
    '''
    cheltuiala['data'] = data


def get_tipul(cheltuiala):
    '''

    :param cheltuiala: Dict
    :return: tipul - string
    '''
    # return cheltuiala[4]
    return cheltuiala['tipul']


def set_tipul(cheltuiala, tipul):
    '''
    Setarea tipul la prajitura
    :param cheltuiala: Dict
    :param tipul: string
    :return:
    '''
    cheltuiala['tipul'] = tipul

def get_zi(cheltuiala):
    data = get_data(cheltuiala)
    data_list = data.split(".")
    return data_list[0]

def get_luna(cheltuiala):
    data = get_data(cheltuiala)
    data_list = data.split(".")
    return data_list[1]

def get_an(cheltuiala):
    data = get_data(cheltuiala)
    data_list = data.split(".")
    return data_list[2]


def to_str(cheltuiala):
    return f'id={get_id(cheltuiala)}, numar_apartament={get_numar_apartament(cheltuiala)}, suma={get_suma(cheltuiala)}' \
           f'data={get_data(cheltuiala)}, tip={get_tipul(cheltuiala)}'
