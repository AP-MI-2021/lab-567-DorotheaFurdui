from Logic.crud import add_cheltuiala
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

