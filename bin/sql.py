from bin.config import config
import psycopg2
import os
import paths

def querySelect(sql):
    
    try:
        conn = None
        params = config(filename=paths.db,section='postgresql')
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

def queryInsertDeck(name,formato):
    sql = """INSERT INTO mtg_schema.decks(name,format) VALUES(%s,%s) RETURNING id"""
    conn = None
    try:
        params = config(filename=paths.db,section='postgresql')
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql,(name,formato))
        id_row = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
    
    return id_row

def queryInsertDeckCards(id_deck,card_name,cant,sideboard):
    sql = """INSERT INTO mtg_schema.deckcards(id_deck,card_name,cant,side) VALUES(%s,%s,%s,%s)"""
    conn = None
    try:
        params = config(filename=paths.db,section='postgresql')
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql,(id_deck,card_name,cant,sideboard))
        conn.commit()
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
 
def queryDeleteDecks():
    sql = """DELETE FROM mtg_schema.decks"""
    conn = None
    try:
        params = config(filename=paths.db,section='postgresql')
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()  
 
def insertDecks(tipo):
    filelist = os.listdir(paths.deck + tipo)
    for i in range(len(filelist)):
        line = filelist[i]
        name = str(line[7:-4])
        formato = str(tipo[:-1])
        id_row = queryInsertDeck(name,formato)
        file = paths.deck + tipo + line
        side = "N"
        with open(file,"r") as fl:
            for l in fl:
                if l[0] == '\n':
                    side = "Y"
                else:
                    cant = int(l[0])
                    card = l[2:]
                    queryInsertDeckCards(id_row, card, cant, side)
                

def buscarCarta(carta):
    card_control = ""
    consulta = "select * from mtg_schema.cards where name like '{0}' order by name".format(carta.lower().capitalize())
    result = querySelect(consulta)
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