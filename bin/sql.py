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
    
if __name__ == '__main__':
    
    carta = input("Ingrese el nombre de la carta: ")
    consulta = "select * from mtg_schema.cards where name = '{0}'".format(carta)
    result = query(consulta)
    if result == '':
        print("Resultado Encontrados:")
        row = result[0]
        name, expa, cardtype, rarity, manacost, converted, power, defense, loyalty, ability = row[1:11]
        print("Nombre: ",name)
        print("Expansion: ", expa)
        print("Tipo: ", cardtype)
        print("Coste: ", manacost)
        print("Fuerza: ", power)
        print("Defensa: ", defense)
        print("Habilidad:", ability)
    else:
        print("No se encontraron resultados")