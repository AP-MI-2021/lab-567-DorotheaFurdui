from Domain.cheltuiala import to_str
from Logic.crud import add_cheltuiala

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
        add_cheltuiala(cheltuieli, id, numar_apartament, suma, data, tipul)
        print('Cheltuiala a fost adaugata cu succes')

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_cheltuiala_userinterface(cheltuieli)
        elif cmd == '4':
            handle_show_all(cheltuieli)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida")


def run_operatiuni_userinterface(cheltuieli):
    pass

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