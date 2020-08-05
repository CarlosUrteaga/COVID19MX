import json
ENTIDADES = json.load(open("../src/diccionario_datos_covid19/ENTIDADES.jsn"))
MUNICIPIOS = json.load(open("../src/diccionario_datos_covid19/MUNICIPIOS.jsn"))
NACIONALIDAD = json.load(open("../src/diccionario_datos_covid19/NACIONALIDAD.jsn"))
ORIGEN = json.load(open("../src/diccionario_datos_covid19/ORIGEN.jsn"))
RESULTADO = json.load(open("../src/diccionario_datos_covid19/RESULTADO.jsn"))
SECTOR = json.load(open("../src/diccionario_datos_covid19/SECTOR.jsn"))
SEXO = json.load(open("../src/diccionario_datos_covid19/SEXO.jsn"))
SI_NO = json.load(open("../src/diccionario_datos_covid19/SI_NO.jsn"))
TIPO_PACIENTE = json.load(open("../src/diccionario_datos_covid19/TIPO_PACIENTE.jsn"))
COLUMNS_REPORT = ['date', 'activos', 'positivos', 'muertes', 'sospechosos', 'muestra', 'activos sospechosos', 'defunciones sospechosos', 'muertos negativos']