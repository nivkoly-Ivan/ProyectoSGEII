from logs import Log
import menu
log = Log()

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# bugfix002 - Ismael
# Una vez se inicia el main, ahora si lleva al menu inicio
if __name__ == '__main__':
    log.escribir("INFO-INICIO","INICIO DE APLICACIÓN")
    menu.menu_inicio()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
