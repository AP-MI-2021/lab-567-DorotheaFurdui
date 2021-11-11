from Domain.cheltuiala import to_str
from Logic.crud import add_cheltuiala, edit_cheltuiala, delete_cheltuiala
from Logic.operatiuni import stergere_toate_cheltuieli, add_valoare, cea_mai_mare_cheltuiala, ordonare_cheltuieli


def print_meniu():
    print('''
        MENIU
        1. CRUD 
        2. Operatiuni
        3. Undo/Redo
        x. Iesire
        ''')

def print_crud_meniu():
    print('''
    MENIU Crud
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate cheltuielile
    5. Inapoi
    ''')

def print_operatiuni_meniu():
    print('''
    Meniu Operatiuni
    1. Stergerea tuturor cheltuielilor unui apartament dat.
    2. Adunarea unei valori la toate cheltuielile dintr-o dată citită.
    3. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
    4. Ordonarea cheltuielilor descrescător după sumă.
    5. Afișarea sumelor lunare pentru fiecare apartament.
    6. Inapoi
    ''')

def run_crud_userinterface(cheltuieli):
    '''

    :param cheltuieli: lista de cheltuieli
    :return:
    '''

    def handle_show_all(cheltuieli):
        '''
        Afiseaza lista de cheltuieli din memorie
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        for cheltuiala in cheltuieli:
            print(to_str(cheltuiala))

    def handle_edit_cheltuiala_userinterface(cheltuieli):
        '''
        Modificam o cheltuiala
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id = input('Dati idul cheltuelii pe care vreti sa o modificati: ')
        numar_apartament = input('Dati numarul apartamentului: ')
        suma = input('Dati suma: ')
        data = input('Dati data: ')
        tipul = input('Dati tipul: ')
        try:
            cheltuieli = edit_cheltuiala(cheltuieli, id, numar_apartament, suma, data, tipul)
            print('Cheltuiala a fost modificata cu succes')
            return cheltuieli
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_add_cheltuiala_userinterface(cheltuieli):
        '''
        Adaugam o cheltuiala citita de la tastatura in lista de cheltuieli
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id = input('Dati idul cheltuelii')
        numar_apartament = int(input('Dati numarul apartamentului'))
        suma = float(input('Dati suma'))
        data = input('Dati data')
        tipul = input('Dati tipul')
        try:
            cheltuieli = add_cheltuiala(cheltuieli, id, numar_apartament, suma, data, tipul)
            print('Cheltuiala a fost adaugata cu succes')
            return cheltuieli
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')
        finally:
            pass
            # codul de aici se executa si daca a fost functia executata cu succes si si daca au aparut erori

    def handle_delete_cheltuiala_userinterface(cheltuieli):
        '''
        Stergem o cheltuiala
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id_cheltuiala = input('Dati idul cheltuelii pe care vreti sa o stergeti')
        cheltuieli_new = delete_cheltuiala(cheltuieli, id_cheltuiala)
        print("Stergerea a avut loc cu succes!")
        return cheltuieli_new

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_cheltuiala_userinterface(cheltuieli)
        elif cmd == '2':
            handle_edit_cheltuiala_userinterface(cheltuieli)
        elif cmd == '3':
            handle_delete_cheltuiala_userinterface(cheltuieli)
        elif cmd == '4':
            handle_show_all(cheltuieli)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida")


def run_operatiuni_userinterface(cheltuieli):
    '''

    :param cheltuieli: lista de cheltuieli
    :return:
    '''

    def handle_stergere_toate_cheltuieli(cheltuieli):
        '''
        Stergerea tuturor cheltuielilor unui apartament dat
        :param cheltuieli: lista
        :return:
        '''
        numar_apartament = int(input("Dati numarul apartamentului unde vreti sa stergeti toate cheltuielile: "))
        cheltuieli_new = stergere_toate_cheltuieli(cheltuieli, numar_apartament)
        print("Toate cheltuielile pentru apartamentul introdus au fost sterse cu succes!")
        return cheltuieli_new

    def handle_add_valoare(cheltuieli):
        '''

        :param cheltuieli:
        :return:
        '''
        data = input("Introduceti data la care doriti sa adaugati o valoare: ")
        valoare = float(input("Introduceti valoarea pe care doriti sa o adaugati: "))
        cheltuieli = add_valoare(cheltuieli, data, valoare)
        print("Valoarea a fost adaugata cu succes!")
        return cheltuieli

    def handle_cea_mai_mare_cheltuiala(cheltuieli):
        '''

        :param cheltuieli:
        :return:
        '''
        result = cea_mai_mare_cheltuiala(cheltuieli)
        for tipul in result:
            print("Tipul {} are cheltuiala(suma) maxima: {}".format(tipul, result[tipul]))

    def handle_ordonare_cheltuieli(cheltuieli):
        '''

        :param cheltuieli:
        :return:
        '''
        cheltuieli = ordonare_cheltuieli(cheltuieli)
        print('Ordonarea s-a facut cu succes!')
        return cheltuieli


    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            cheltuieli = handle_stergere_toate_cheltuieli(cheltuieli)
        elif cmd == '2':
            cheltuieli = handle_add_valoare(cheltuieli)
        if cmd == '3':
            handle_cea_mai_mare_cheltuiala(cheltuieli)
        elif cmd == '4':
            cheltuieli = handle_ordonare_cheltuieli(cheltuieli)
        if cmd == '5':
            pass
           # cheltuieli = handle_show_sume_lunare(cheltuieli)
        elif cmd == '6':
            run_console(cheltuieli)
        else:
            print("Comanda invalida")


def run_undo_redo_userinterface(cheltuieli):
    pass


def run_console(cheltuieli):
    '''

    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_userinterface(cheltuieli)
        elif cmd == '2':
            run_operatiuni_userinterface(cheltuieli)
        elif cmd == '3':
            run_undo_redo_userinterface(cheltuieli)
        elif cmd == 'x':
            print("La revedere!")
            break
        else:
            print("Comanda invalida")