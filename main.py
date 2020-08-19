import requests
import os
import wget
import shutil
import paths

def armadoBaseline():
    os.makedirs(paths.tmp)
    webModern = requests.get(paths.webModern)
    webPioneer = requests.get(paths.webPioneer)
    webStandard = requests.get(paths.webStandard)
    open(paths.tmpModern,"w").write(webModern.text)
    open(paths.tmpPioneer,"w").write(webPioneer.text)
    open(paths.tmpStandard,"w").write(webStandard.text)
    descargaBD(paths.tmpModern,"modern/")
    descargaBD(paths.tmpPioneer,"pioneer/")
    descargaBD(paths.tmpStandard,"standard/")

def descargaBD(file, tipo):
    os.makedirs(paths.tmp + tipo)
    path = paths.tmp + tipo
    with open(file,"r") as fl:
        for line in fl:
            inicio = line.find('<a href="/archetype/')
            if(inicio == 0 and ("#paper" in line)):
                fin = line.find('#paper')
                corte = line.find('">')
                deck = requests.get(paths.mainWeb + "archetype/" +line[20:corte])
                with open(path + line[20:fin],"w",encoding='utf-8') as f:
                    f.write(deck.text)

def descargaDecks(tipo):
    filelist = os.listdir(paths.tmp + tipo)
    shutil.rmtree(paths.deck + tipo)
    os.makedirs(paths.deck + tipo)
    for file in filelist:
        with open(os.path.join(paths.tmp + tipo, file),"r",encoding='utf-8') as file2:
            for line in file2:
                vD = line.find("/deck/download/")
                vD2 = line.find('">')
                if (vD != -1) and (vD2 != -1):
                    deck2 = line[vD:vD2]
                    pagina2 = paths.mainWeb + deck2
                    wget.download(pagina2, out=paths.deck + tipo)
                     
                 
if __name__ == '__main__':
    print("Iniciando Sistema de Chequeo de Decks")
    print("Sincronizando datos...")
    armadoBaseline()
    print("Sincronizacion Completada")
    print("Comenzando descarga de Decks...")
    descargaDecks("modern/")
    print("Descarga de Decks de Modern Completa")
    descargaDecks("pioneer/")
    print("Descarga de Decks de Pioneer Completa")
    descargaDecks("standard/")
    print("Descarga de Decks de Standard Completa")
    shutil.rmtree(paths.tmp)
    print("Descarga de Decks Finalizada")
    