from Domain.cheltuiala import create_cheltuiala

def add_cheltuiala(cheltuieli, id, numar_apartament, suma, data, tipul):
    '''
    Adaugam in memorie in lista de cheltuieli o cheltuiala formata din fieldurile: id, numar_apartament, suma, data, tipul
    :param cheltuieli: lista de cheltuieli
    :param id: string
    :param numar_apartament: int
    :param suma: float
    :param data: string
    :param tipul: string
    :return:
    '''

    cheltuiala = create_cheltuiala(id, numar_apartament, suma, data, tipul)
    cheltuieli.append(cheltuiala)