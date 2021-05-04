import csv
import os.path
import os
import json

def top10_sales_JP(path_arch,archivo_ventas):
        with open(os.path.join(path_arch,archivo_ventas),encoding='utf-8') as ventas_jp:
            datos_estruct = []

            for i in csv.DictReader(ventas_jp):
                datos_estruct.append(dict(i))
        conj = sorted(datos_estruct, key=lambda k: k['JP_Sales'],reverse=True)

        conj_2= list((map(lambda x: x['Name'], conj[:10])))

        save((conj_2[:10]),"JP_Sales_Top10")

def top10_rating_albums(path_arch,archivo_ventas):
        with open(os.path.join(path_arch,archivo_ventas),encoding='utf-8') as rating_albums:
            datos_estruct = []

            for i in csv.DictReader(rating_albums):
                datos_estruct.append(dict(i))
        conj = sorted(datos_estruct, key=lambda k: k['rating'],reverse=True)

        conj_2= list((map(lambda x: x['name'], conj[:10])))

        save((conj_2[:10]),"Albums_Rating_Top10")

def save(lista,key):
    WORDS_FILE_PATH = os.path.join(os.getcwd(), "data", "words.json")
    with open(WORDS_FILE_PATH, 'w') as users_file:
        new_item= {f"{key}": lista}
        json.dump(new_item, users_file)

