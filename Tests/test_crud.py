from Logic.crud import add_cheltuiala, edit_cheltuiala, find_cheltuiala, delete_cheltuiala
from Domain.cheltuiala import create_cheltuiala, get_id, get_numar_apartament, get_suma, get_data, get_tipul

def test_add_cheltuiala():
    cheltuieli = []
    cheltuiala_adaugata = create_cheltuiala('12A', 7, 147.47, '16.06.2020', 'apa')
    add_cheltuiala(cheltuieli, '12A', 7, 147.47, '16.06.2020', 'apa')
    assert len(cheltuieli) == 1
    assert cheltuieli[0] == cheltuiala_adaugata
    assert get_id(cheltuieli[0]) == '12A'
    assert get_numar_apartament(cheltuieli[0]) == 7
    assert get_suma(cheltuieli[0]) == 147.47
    assert get_data(cheltuieli[0]) == '16.06.2020'
    assert get_tipul(cheltuieli[0]) == 'apa'

    add_cheltuiala(cheltuieli, '4', 8, 534.6, '10.10.2019', 'curent')
    cheltuiala_adaugata_2 = create_cheltuiala('4', 8, 534.6, '10.10.2019', 'curent')
    assert len(cheltuieli) == 2
    assert cheltuieli[0] == cheltuiala_adaugata
    assert cheltuieli[1] == cheltuiala_adaugata_2

def test_edit_cheltuiala():
    c1 = create_cheltuiala('12A', 7, 147.47, '16.06.2020', 'apa')
    c2 = create_cheltuiala('7A', 10, 167.47, '16.06.2020', 'intretinere')
    cheltuieli = [c1, c2]
    assert len(cheltuieli) == 2
    cheltuieli = edit_cheltuiala(cheltuieli, '12A', 16, 102.47, '16.06.2020', 'apa new')
    assert len(cheltuieli) == 2
    c1_new = find_cheltuiala(cheltuieli, '12A')
    assert get_numar_apartament(c1_new) == 16
    assert get_suma(c1_new) == 102.47
    assert get_data(c1_new) == '16.06.2020'
    assert get_tipul(c1_new) == 'apa new'

def test_delete_cheltuiala():
    c1 = create_cheltuiala('12A', 7, 147.47, '16.06.2020', 'apa')
    c2 = create_cheltuiala('7A', 10, 167.47, '16.06.2020', 'intretinere')
    cheltuieli = [c1, c2]
    assert len(cheltuieli) == 2
    cheltuieli = delete_cheltuiala(cheltuieli, '12A')
    assert len(cheltuieli) == 1
    cheltuieli = delete_cheltuiala(cheltuieli, '12Abc')
    assert len(cheltuieli) == 1



