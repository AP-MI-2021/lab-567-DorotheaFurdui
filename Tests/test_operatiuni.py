from Logic.crud import *
from Logic.operatiuni import *
from Domain.cheltuiala import create_cheltuiala

def test_stergere_toate_cheltuieli():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 1, 1, 120.9, '04.06.2002', 'alte cheltuieli')
    cheltuieli = add_cheltuiala(cheltuieli, 2, 4, 120.9, '04.07.2002', 'alte cheltuieli')
    cheltuieli = add_cheltuiala(cheltuieli, 3, 4, 145.8, '04.07.2002', 'alte cheltuieli')
    assert len(cheltuieli) == 3
    cheltuieli = stergere_toate_cheltuieli(cheltuieli, 4)
    assert len(cheltuieli) == 1

def test_add_valoare():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 1, 4, 132.14, "23.01.2021", "canal")
    cheltuieli = add_cheltuiala(cheltuieli, 2, 16, 155, "07.06.2002", "intretinere")
    cheltuieli = add_cheltuiala(cheltuieli, 3, 12, 98.5, "13.06.2002", "alte cheltuieli")

    cheltuieli = add_valoare(cheltuieli, "07.06.2002", 10)
    assert len(cheltuieli) == 3
    assert get_suma(cheltuieli[0]) == 132.14
    assert get_suma(cheltuieli[1]) == 165
    assert get_suma(cheltuieli[2]) == 98.5

def test_cea_mai_mare_cheltuiala():
    lista = []
    lista = add_cheltuiala(lista, 'id1', 1, 450.2, '25.06.2002', 'alte cheltuieli')
    lista = add_cheltuiala(lista, 'id2', 9, 242.45, '18.09.2002', 'intretinere')
    lista = add_cheltuiala(lista, 'id3', 9, 192.17, '18.09.2002', 'intretinere')
    rezultat = cea_mai_mare_cheltuiala(lista)

    assert len(rezultat) == 2
    assert rezultat['alte cheltuieli'] == 450.2
    assert rezultat['intretinere'] == 242.45

def test_ordonare_cheltuieli():
    p1 = create_cheltuiala('id2', 1, 345, '25.06.2002', 'alte cheltuieli')
    p2 = create_cheltuiala('id2', 6, 86.54, '18.09.2002', 'alte cheltuieli')
    p3 = create_cheltuiala('id1', 7, 576.2, '18.11.2021', 'alte cheltuieli')

    ordonare_list = ordonare_cheltuieli([p1, p2, p3])
    assert ordonare_list[0] == p3
    assert ordonare_list[1] == p1
    assert ordonare_list[2] == p2




