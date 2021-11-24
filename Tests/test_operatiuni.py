from Logic.crud import *
from Logic.operatiuni import *
from Domain.cheltuiala import create_cheltuiala


def test_stergere_toate_cheltuieli():
    cheltuieli = []
    add_cheltuiala(cheltuieli, 1, 1, 120.9, '04.06.2002', 'alte cheltuieli')
    add_cheltuiala(cheltuieli, 2, 4, 120.9, '04.07.2002', 'alte cheltuieli')
    add_cheltuiala(cheltuieli, 3, 4, 145.8, '04.07.2002', 'alte cheltuieli')
    assert len(cheltuieli) == 3
    stergere_toate_cheltuieli(cheltuieli, 4)
    assert len(cheltuieli) == 1


def test_add_valoare():
    cheltuieli = []
    add_cheltuiala(cheltuieli, 1, 4, 132.14, "23.01.2021", "canal")
    add_cheltuiala(cheltuieli, 2, 16, 155, "07.06.2002", "intretinere")
    add_cheltuiala(cheltuieli, 3, 12, 98.5, "13.06.2002", "alte cheltuieli")

    add_valoare(cheltuieli, "07.06.2002", 10)
    assert len(cheltuieli) == 3
    assert get_suma(cheltuieli[0]) == 132.14
    assert get_suma(cheltuieli[1]) == 165
    assert get_suma(cheltuieli[2]) == 98.5


def test_cea_mai_mare_cheltuiala():
    lista = []
    add_cheltuiala(lista, 'id1', 1, 450.2, '25.06.2002', 'alte cheltuieli')
    add_cheltuiala(lista, 'id2', 9, 242.45, '18.09.2002', 'intretinere')
    add_cheltuiala(lista, 'id3', 9, 192.17, '18.09.2002', 'intretinere')
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


def test_cheltuieli_lunare():
    list_cheltuieli = []
    for index in range(1, 10):
        p = create_cheltuiala(f"id{index}", numar_apartament=index, suma=index * 7, data=f"10.0{index}.2020",
                              tipul="apa")
        list_cheltuieli.append(p)
        p1 = create_cheltuiala(f"id1{index}", numar_apartament=index, suma=index * 7, data=f"15.0{index}.2021",
                              tipul="apa")
        list_cheltuieli.append(p1)
        p2 = create_cheltuiala(f"id2{index}", numar_apartament=index, suma=index * 7, data=f"12.0{index}.2020",
                              tipul="apa")
        list_cheltuieli.append(p2)
    result = cheltuieli_lunare(list_cheltuieli)
    for index in range(1, 10):
        assert result[index]["2021"][f"0{index}"] == index*7
        assert result[index]["2020"][f"0{index}"] == index*7*2

def test_undo_redo():
    list_cheltuieli = []
    istoric.clear()
    istoric_redo.clear()
    for index in range(1,4):
        add_cheltuiala(list_cheltuieli,index,index,index*7,f"10.0{index}.2020","apa")

    for index in range(3,0,-1):
        assert len(list_cheltuieli)==index
        assert list_cheltuieli[-1]["id"]==index
        undo(list_cheltuieli)
    assert len(list_cheltuieli) == 0

    try:
        undo(list_cheltuieli)
        exception_thrown=False
    except:
        exception_thrown=True
    finally:
        assert exception_thrown == True

    for index in range(1,4):
        add_cheltuiala(list_cheltuieli,index,index,index*7,f"10.0{index}.2020","apa")
    try:
        redo(list_cheltuieli)
        exception_thrown=False
    except:
        exception_thrown=True
    finally:
        assert exception_thrown == True

    undo(list_cheltuieli)
    undo(list_cheltuieli)
    assert len(list_cheltuieli) == 1
    for index in range(2,4):
        redo(list_cheltuieli)
        assert len(list_cheltuieli) == index
        assert list_cheltuieli[-1]["id"] == index
    undo(list_cheltuieli)
    undo(list_cheltuieli)
    assert len(list_cheltuieli) == 1
    add_cheltuiala(list_cheltuieli,4,4,4*7,f"10.0{4}.2020","apa")
    try:
        redo(list_cheltuieli)
        exception_thrown=False
    except:
        exception_thrown=True
    finally:
        assert exception_thrown == True
    undo(list_cheltuieli)
    undo(list_cheltuieli)
    assert len(list_cheltuieli) == 0
    redo(list_cheltuieli)
    redo(list_cheltuieli)
    assert len(list_cheltuieli) == 2
    try:
        redo(list_cheltuieli)
        exception_thrown=False
    except:
        exception_thrown=True
    finally:
        assert exception_thrown == True
