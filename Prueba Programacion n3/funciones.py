


def agregar_libro (a:str, b:dict) :
    for i in b:
        if i == "Libro":
            b[i].append({"Titulo" : a})
    return print(b["Libro"])


def modificar_libro (a:int, b:dict) :
    for i in b:
        if i == "Libro":
            for l in b[i]:
                for m in l:
                    imp = print(m)
                        
    return print(imp)
