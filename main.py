
from src.menus import menu, menu_principal,menu_pizzas,menu_bebidas,menu_otros # carpeta.carpeta., etc para importar
from src.modulos.catalogo_productos import obtener_catalogo
from src.modulos.calculos import calculo_precio_pizzas
from src.modulos.cambiar_temporada import cambiar_temporada


opcion_general = menu_principal()

while opcion_general > 0 and opcion_general < 4:

    match opcion_general:
        case 1: # opcion seleccionada pizza
            o_pizas = menu_pizzas()

            match o_pizas: # selecciona la funcion que se encarga de esta parte
                case 1:
                    obtener_catalogo()
                        
                case 2:
                    calculo_precio_pizzas()
                        
                case 3:
                    print("en desarrollo")
                        
           
                    
        case 2:  # seleccionado temporadas
            print("desarrollo")
        case 3: # otros
             cambiar_temporada()
        
    opcion_general = menu_principal()
                
                    





