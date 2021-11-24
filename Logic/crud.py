import copy
from copy import deepcopy

from Domain.cheltuiala import *
from Domain.cheltuiala import create_cheltuiala, get_id, set_numar_apartament, set_suma, set_data, set_tipul
from Logic.validator import validate_cheltuiala

istoric = []
istoric_redo=[]

def find_cheltuiala(cheltuieli, id):
    '''
    Gaseste cheltuiala in cheltuieli cu id. Daca nu gaseste, returneaza None
    :param cheltuieli:
    :param id:
    :return:
    '''
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def edit_cheltuiala(cheltuieli, id, numar_apartament_new, suma_new, data_new, tipul_new):
    '''
    Editarea cheltuieli cu idul id si aruncarea unei erori ValueError in cazul in care fieldurile nu sunt
    corecte
    :param cheltuieli: lista de cheltuieli
    :param id: string
    :param numar_apartament_new: int
    :param suma_new: int
    :param data_new: string
    :param tipul_new: string
    :return:
    '''
    add_istoric(cheltuieli)
    istoric_redo.clear()
    id, nr_ap_new, suma_new, data_new, tipul_new = validate_cheltuiala(id, numar_apartament_new, suma_new, data_new,
                                                                       tipul_new)
    updated_list = deepcopy(cheltuieli)
    for cheltuiala in updated_list:
        if get_id(cheltuiala) == id:
            set_numar_apartament(cheltuiala, numar_apartament_new)
            set_suma(cheltuiala, suma_new)
            set_data(cheltuiala, data_new)
            set_tipul(cheltuiala, tipul_new)
    cheltuieli[:] = updated_list


def add_cheltuiala(cheltuieli, id, numar_apartament, suma, data, tipul):
    '''
    Adaugam in memorie in lista de cheltuieli o cheltuiala formata din fieldurile: id, numar_apartament, suma, data, tipul
    :param cheltuieli: lista de cheltuieli
    :param id: string
    :param numar_apartament: int
    :param suma: int
    :param data: string
    :param tipul: string
    :return:
    '''
    add_istoric(cheltuieli)
    istoric_redo.clear()
    id, numar_apartament, suma, data, tipul = validate_cheltuiala(id, numar_apartament, suma, data, tipul)
    cheltuiala = create_cheltuiala(id, numar_apartament, suma, data, tipul)
    cheltuieli.append(cheltuiala)


def delete_cheltuiala(cheltuieli, id):
    '''
    Stergerea unei cheltuieli cu idul id
    :param cheltuieli:
    :param id:
    :return:
    '''
    add_istoric(cheltuieli)
    istoric_redo.clear()
    result_list = [cheltuiala for cheltuiala in cheltuieli if get_id(cheltuiala) != id]
    cheltuieli[:] = result_list

def add_istoric(cheltuieli):
    istoric.append(copy.deepcopy(cheltuieli))
