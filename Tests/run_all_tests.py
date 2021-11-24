from Tests.test_crud import test_add_cheltuiala, test_edit_cheltuiala, test_delete_cheltuiala
from Tests.test_operatiuni import test_stergere_toate_cheltuieli, test_add_valoare, test_cea_mai_mare_cheltuiala, \
    test_ordonare_cheltuieli, test_cheltuieli_lunare, test_undo_redo


def run_all_tests():
    test_add_cheltuiala()
    test_edit_cheltuiala()
    test_delete_cheltuiala()
    test_stergere_toate_cheltuieli()
    test_add_valoare()
    test_cea_mai_mare_cheltuiala()
    test_ordonare_cheltuieli()
    test_cheltuieli_lunare()
    test_undo_redo()
