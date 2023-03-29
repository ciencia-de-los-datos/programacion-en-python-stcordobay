"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def extract_table(path="./data.csv"):
    with open("./data.csv", "r") as file:
        datos = file.readlines()
        datos = list(map(lambda x:x.replace("\t", ".").split('.') ,datos))
    return datos

def pregunta_01(path="./data.csv"):
    """
    Retorne la suma de la segunda columna.
    
    """
    datos=extract_table()
    c=sum(list(map(int, list(zip(*datos))[1])))
    return(c)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos=extract_table()
    contar=[]
    for i in sorted(set(list(list(zip(*datos))[0]))):
        contar.append((i, list(list(zip(*datos))[0]).count(i)))
    return contar


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import itertools
    datos=extract_table()
    key_and_sum=[]
    an_iterator=itertools.groupby(sorted(datos), lambda x:x[0])
    for key, group in an_iterator:
        key_and_sum.append((key,sum((list(map(lambda x: int(x[1]) ,list(group)))))))
    return key_and_sum


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    datos=extract_table()
    meses=list(map(lambda x: x[2].split('-')[1], datos))
    mes=[]
    for i in sorted(set(meses)):
        mes.append((i,meses.count(i)))
    return mes


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import itertools
    datos=extract_table()
    key_min_max=[]
    an_iterator=itertools.groupby(sorted(datos), lambda x:x[0])
    for key, group in an_iterator:
        g=list(group)
        key_min_max.append((key,max((list(map(lambda x: int(x[1]) ,g)))),min((list(map(lambda x: int(x[1]) ,g))))))
    return key_min_max


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import itertools
    datos=extract_table()
    col5=list(itertools.chain.from_iterable(list(map(lambda y: y.split(','), 
                                                     list(map(lambda x: x.split("\n")[0], list(zip(*datos))[4]))))))
    an_iterator=itertools.groupby(sorted(col5), lambda x:x.split(':')[0])
    letter=[]
    for key, group in an_iterator:
        dat=list(group)
        letter.append((key, 
                       min(list(map(lambda x:int(x.split(':')[1]), dat))), 
                       max(list(map(lambda x:int(x.split(':')[1]), dat)))))
    return letter


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos=extract_table()
    number=[]
    for i in sorted(set(list(map(lambda x: int(x[1]),datos)))):
        letter=[]
        filterdata=list(map(lambda x: letter.append(x[0]) if (x[1]==str(i)) else None,datos))
        number.append((i, letter))
    return number


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    number=pregunta_07()
    s=[]
    list(map(lambda x: s.append((x[0], sorted(set(x[1])))),number))
    return s


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import itertools
    datos=extract_table()
    col5=list(itertools.chain.from_iterable(list(map(lambda y: y.split(','), 
                                                     list(map(lambda x: x.split("\n")[0], list(zip(*datos))[4]))))))
    an_iterator=itertools.groupby(sorted(col5), lambda x:x.split(':')[0])
    nletter={}
    for key, group in an_iterator:
        dat=list(group)
        nletter[key]=len(dat)
    return nletter


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos=extract_table()
    lendat=[]
    list(map(lambda x: lendat.append((x[0],len(x[3].split(',')),len(x[4].split(',')))), datos)) 
    return lendat


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import itertools
    datos=extract_table()
    col4=list(itertools.chain.from_iterable(list(map(lambda y: y.split(','), 
                                                         list(map(lambda x: x.split("\n")[0], list(zip(*datos))[3]))))))
    dictionary={}
    for i in sorted(set(col4)):
        dictionary[i]=sum(list(map(lambda x: int(x[1]), filter(lambda x: True if i in x[3].split(',') else False, datos))))

    return dictionary


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import itertools
    datos=extract_table()
    key_sum4={}
    an_iterator=itertools.groupby(sorted(datos), lambda x:x[0])
    for key, group in an_iterator:
        suma=0
        for j in list(map(lambda y:y[4].split(','), list(group))):
            suma=suma+sum(list(map(lambda x: int(x.split(':')[1].replace('\n','')), j)))
        key_sum4[key]=suma
    return key_sum4
