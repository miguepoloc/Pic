import csv

lista_id = []  # Lista vacía
diccionario_id = {}  # Diccionario vacío
cabecera = ["Nombre completo", "Documento de Identidad",
            "No. Documento", "Celular", "Municipio", "Dirección"]

with open('D:/Codigos/datos.csv', newline='', encoding='utf-8') as csvfile:
    prueba_lista = []
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        if row["Seccion"] == "IDENTIFICACIÓN DEL JEFE DE HOGAR Y DELINTEGRANTE QUE RECIBE LA VISITA" or row["Seccion"] == "IDENTIFICACION DEL HOGAR":
            if row["\ufeffId Ficha"][0:6] in lista_id:
                pass
            else:
                lista_id.append(row["\ufeffId Ficha"][0:6])
                diccionario_id[row["\ufeffId Ficha"][0:6]] = {'Nombre completo': "SD", 'Documento de Identidad': "SD",
                                                              'No. Documento': "SD", 'Celular': "SD", "Municipio": "SD", "Dirección": "SD"}

            if row["Pregunta"] in cabecera:

                if row["Pregunta"] == "Municipio" or row["Pregunta"] == "Documento de Identidad":
                    diccionario_id[row["\ufeffId Ficha"][0:6]
                                   ][row["Pregunta"]] = row["Opcion"]
                else:
                    diccionario_id[row["\ufeffId Ficha"][0:6]
                                   ][row["Pregunta"]] = row["Valor"]


with open('datos_dep.csv', 'w', newline='',  encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=cabecera)

    writer.writeheader()
    for v in diccionario_id.values():
        writer.writerow(v)
