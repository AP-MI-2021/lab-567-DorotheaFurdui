from Logic.operatiuni import populare
from UserInterface.consola import run_console
from Tests.run_all_tests import run_all_tests

def main():
    cheltuieli = populare()
    run_console(cheltuieli)
run_all_tests()
main()
