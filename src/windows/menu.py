import PySimpleGUI as sg


sg.theme('DarkTeal6')

letter="Arial 20 bold"
letter_2="Arial 12 bold"

sg.set_options(element_padding=(0, 5))

def build():
    """
    Construye la ventana del menú
    """
    layout = [
        [sg.Text("¿Que datos analizamos?",size=(30,0),font=letter,justification='center')],
        [sg.Button('Ventas de videojuegos',font=letter_2, size=(23, 3), key="-csv1-")],
        [sg.Button('Top 500 Albums of all Time - Rate Your Music',font=letter_2, size=(23, 3), key="-csv2-")],
        [sg.Button('Salir',font=letter_2, size=(23, 3), key="-exit-")]
    ]

    board = sg.Window('MemPy', layout, location=(630,350),finalize=True,element_justification="center",size=(480,350))

    return board