
from src.menus import menu, menu_principal,menu_pizzas,menu_bebidas,menu_otros # carpeta.carpeta., etc para importar
from src.modulos.catalogo_productos import obtener_catalogo
from src.modulos.calculos import calculo_precio_pizzas

opcion_general = menu_principal()

while opcion_general > 0 and opcion_general < 4:

    match opcion_general:
        case 1:
            o_pizas = menu_pizzas()

            while o_pizas > 0 and o_pizas < 4:

                match o_pizas:
                    case 1:
                        obtener_catalogo()
                        
                    case 2:
                        calculo_precio_pizzas()
                        
                    case 3:
                        print("en desarrollo")
                        
                o_pizas = menu_pizzas()
                    
        case 2:
            print("desarrollo")
        case 3:
            print("desarrollo")
        
    opcion_general = menu_principal()
                
                    





