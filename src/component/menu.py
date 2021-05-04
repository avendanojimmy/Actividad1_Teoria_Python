import PySimpleGUI as sg
from src.windows import menu
import csv
import os.path
import os
from src.component import search

def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    path_files = "data"
    archivo_ventas = "vgsales.csv"
    archivo_albums = "rym_top_500_albums.csv"
    path_arch = os.path.join(os.getcwd(), path_files)
    window = menu.build()
    while True:
        event, _values = window.read()
        if event == '-exit-' or event == sg.WIN_CLOSED:
            break
        elif event == "-csv1-":
            search.top10_sales_JP(path_arch,archivo_ventas)
            sg.popup("Se guardaron los nombres de los 10 juegos mas vendidosa en Japon ./data/words.json")
            break
        elif event == "-csv2-":
            search.top10_rating_albums(path_arch,archivo_albums)
            sg.popup("Se guardaron los nombres de los 10 albums con mayor rating en ./data/words.json")
            break

    return window
