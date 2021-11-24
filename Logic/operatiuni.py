import copy

import Logic
from Domain.cheltuiala import get_id, get_numar_apartament, get_suma, get_data, get_tipul, create_cheltuiala, get_luna, \
    get_an
from Logic.crud import add_cheltuiala, istoric, add_istoric, istoric_redo


def stergere_toate_cheltuieli(cheltuieli, numar_apartament_stergere):
    '''
    Stergerea tuturor cheltuielilor pentru un apartament
    :param cheltuieli: lista
    :param numar_apartament_stergere: int
    :return:
    '''
    add_istoric(cheltuieli)
    istoric_redo.clear()
    result = [cheltuiala for cheltuiala in cheltuieli if get_numar_apartament(cheltuiala) != numar_apartament_stergere]
    if len(cheltuieli) == 0:
        raise ValueError('Nu exista nici o cheltuiala pentru acest apartament.')
    cheltuieli[:] = result


def add_valoare(cheltuieli, data_cautata, valoare):
    '''
    Adaugare valoare (la suma) tuturor cheltuielilor pentru o data aleasa.
    :param cheltuieli: lista
    :param data_cautata: string
    :param valoare: float
    :return:
    '''
    add_istoric(cheltuieli)
    istoric_redo.clear()
    result = []
    for cheltuiala in cheltuieli:
        if get_data(cheltuiala) == data_cautata:
            cheltuiala_new = create_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala),
                                               float(get_suma(cheltuiala)) +
                                               valoare, get_data(cheltuiala), get_tipul(cheltuiala))
            result.append(cheltuiala_new)
        else:
            result.append(cheltuiala)
    cheltuieli[:] = result


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
    return sorted(cheltuieli, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)


def cheltuieli_lunare(cheltuieli):
    result = {}
    for cheltuiala in cheltuieli:
        numar = get_numar_apartament(cheltuiala)
        an = get_an(cheltuiala)
        luna = get_luna(cheltuiala)
        suma = get_suma(cheltuiala)
        if numar in result:
            if an in result[numar]:
                if luna in result[numar][an]:
                    result[numar][an][luna] += suma
                else:
                    result[numar][an][luna] = suma
            else:
                result[numar][an] = {luna: suma}
        else:
            result[numar] = {an: {luna: suma}}
    return result


def populare():
    cheltuieli = []
    for index in range(1, 10):
        add_cheltuiala(cheltuieli, f"id2{index}", numar_apartament=index, suma=index * 7, data=f"12.0{index}.2020",
                       tipul="apa")
        add_cheltuiala(cheltuieli, f"id1{index}", numar_apartament=index, suma=index * 8, data=f"12.0{index}.2021",
                       tipul="curent")
        add_cheltuiala(cheltuieli, f"id3{index}", numar_apartament=index, suma=index * 9, data=f"10.0{index}.2020",
                       tipul="intretinere")
    return cheltuieli

def undo(cheltuieli):
    try:
        istoric[-1]
        istoric_redo.append(copy.deepcopy(cheltuieli))
        cheltuieli[:] = istoric[-1]
        istoric.pop()
    except Exception:
        raise Exception("undo imposibil")

def redo(cheltuieli):
    try:
        istoric_redo[-1]
        add_istoric(cheltuieli)
        cheltuieli[:] = istoric_redo[-1]
        istoric_redo.pop()
    except Exception:
        raise Exception("redo imposibil")
