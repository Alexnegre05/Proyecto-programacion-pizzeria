# funcion general para ir comprovando tod el rato el try except
def comprovar_try_except(string):
    
    comprovar = 0 # variable para que en el try except si peta que se reinicie

    while(comprovar == 0):

        try: # ponemso try except
            opcion = int(input(string))
            # solo cuando llega aqui es decir el try except no ha petado podemso salir de el bucle
            comprovar = 1

        except:
            comprovar = 0 # mantenemos comprovar a 0

    return opcion