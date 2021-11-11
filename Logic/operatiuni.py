from Domain.cheltuiala import get_id, get_numar_apartament, get_suma, get_data, get_tipul, create_cheltuiala

def stergere_toate_cheltuieli(cheltuieli, numar_apartament_stergere):
    '''
    Stergerea tuturor cheltuielilor pentru un apartament
    :param cheltuieli: lista
    :param numar_apartament_stergere: int
    :return:
    '''
    result = []
    for cheltuiala in cheltuieli:
        if get_numar_apartament(cheltuiala) != numar_apartament_stergere:
            result.append(cheltuiala)
    if len(cheltuieli) == 0:
        raise ValueError('Nu exista nici o cheltuiala pentru acest apartament.')
    return result

def add_valoare(cheltuieli, data_cautata, valoare):
    '''
    Adaugare valoare (la suma) tuturor cheltuielilor pentru o data aleasa.
    :param cheltuieli: lista
    :param data_cautata: string
    :param valoare: float
    :return:
    '''
    result = []
    for cheltuiala in cheltuieli:
        if get_data(cheltuiala) == data_cautata:
            cheltuiala_new = create_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala), float(get_suma(cheltuiala)) +
                                               valoare, get_data(cheltuiala), get_tipul(cheltuiala))
            result.append(cheltuiala_new)
        else:
            result.append(cheltuiala)
    return result

def cea_mai_mare_cheltuiala(cheltuieli):
    '''

    :param cheltuieli:
    :return:
    '''
    result = {}
    for cheltuiala in cheltuieli:
        tipul = get_tipul(cheltuiala)
        if tipul in result:
            if get_suma(cheltuiala) > result[tipul]:
                result[tipul] = get_suma(cheltuiala)
        else:
            result[tipul] = get_suma(cheltuiala)
    return result

def ordonare_cheltuieli(cheltuieli):
    '''
    Sortare cheltuieli descrescator
    :param cheltuieli: lista
    :return:
    '''
    return sorted(cheltuieli, key = lambda cheltuiala: get_suma(cheltuiala), reverse = True)

def ordonare_criteriu(cheltuiala):
    '''
    :param cheltuiala:
    :return:
    '''
    return get_suma(cheltuiala)
