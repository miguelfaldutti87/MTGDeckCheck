from bin.config import config
import psycopg2

def query(sql):
    
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
 
    return result

def buscarCarta(carta):
    card_control = ""
    consulta = "select * from mtg_schema.cards where name like '{0}' order by name".format(carta.lower().capitalize())
    result = query(consulta)
    if result != []:
        print("Resultado Encontrados:")
        print("")
        for x in range(len(result)):
            row = result[x]
            name, expa, cardtype, rarity, manacost, converted, power, defense, loyalty, ability = row[1:11]
            if card_control != name:
                print("Nombre: ",name)
                print("Expansion: ", expa)
                print("Tipo: ", cardtype)
                print("Coste: ", manacost)
                print("Fuerza: ", power)
                print("Defensa: ", defense)
                print("Habilidad:", ability)
                print("")
                print("")
                card_control = name
    else:
        print("No se encontraron resultados")
    
if __name__ == '__main__':
    
    buscarCarta(input("Ingrese el nombre de la carta: ") + "%")