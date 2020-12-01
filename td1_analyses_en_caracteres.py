"""## Exercice n°3 : Devoir à faire et à déposer en TD"""

import os.path
import glob
import matplotlib
import matplotlib.pyplot as pyplot
import sys
from mosestokenizer import *

textsFolder = "./content/data_languages"


# Meme fonction que pour récupérer les éléments d'un dossier mais la on parcours les sous dossier aussi de façon récursif
def getTextPathMultiDir(dirPath):
    textArray = []
    for item in glob.glob(dirPath + "/*"):
        if os.path.isdir(item):
            textArray.extend(getTextPathMultiDir(item))
        else:
            textArray.append(item)

    return textArray

# Fonction pour remplir le dictionnaire pour pouvoir le faire plus simplement sur les deux livres sans répéter le code
def setDicLongueur(listMots):
  # On créer un dictionnaire vide
  dicLongueurs = {}

  #On parcours le tableau de list de mots - mot par mot
  for mot in listMots :
    longueur = len(mot) # Longueur du mot
    if longueur not in dicLongueurs : #Si elle n'est pas déjà vu
      dicLongueurs[longueur] = 1
    else: # Sinon
      dicLongueurs[longueur] += 1

  return dicLongueurs

def DistribMotSelonTailleV2(listFiles):
  for fileItem in listFiles:
    # Lecture
    fileRead = open(fileItem, "r", encoding="utf-8")
    chaine = fileRead.read()
    fileRead.close()

    # Split
    listMot = chaine.split()

    # Dictionnaire
    dicLongueurs = setDicLongueur(listMot)

    listeEffectifs = []
    for toto in range(30):
      if toto in dicLongueurs:
        listeEffectifs.append(dicLongueurs[toto])
      else:
        listeEffectifs.append(0)

    # pyplot.plot(listeEffectifs)
    # nom_legende= fileItem

    fileName = fileItem.split("/")
    temp = []
    for item in fileName:
        temp.extend(item.split("\\"))
    fileName = temp
    nom_legende = fileName[len(fileName) - 1]
    pyplot.plot(listeEffectifs, label=nom_legende)

  # Ajout de la légende
  pyplot.legend()
  pyplot.title("Une magnifique Courbe")
  pyplot.xlabel("Longueur des Mots")
  pyplot.ylabel("Fréquence")

  # Save du file et affichage
  pyplot.savefig("frequences_V2.png")
  pyplot.show()

def DistribMotSelonTailleV3(listFiles):
    for fileItem in listFiles:
        # Lecture
        fileRead = open(fileItem, "r", encoding="utf-8")
        chaine = fileRead.read()
        fileRead.close()

        # Split
        listMot = chaine.split()
        listMot = set(listMot)

        # Dictionnaire
        dicLongueurs = setDicLongueur(listMot)

        listeEffectifs = []
        for toto in range(30):
            if toto in dicLongueurs:
                listeEffectifs.append(dicLongueurs[toto])
            else:
                listeEffectifs.append(0)

        # pyplot.plot(listeEffectifs)
        # nom_legende= fileItem

        fileName = fileItem.split("/")
        temp = []
        for item in fileName:
            temp.extend(item.split("\\"))
        fileName = temp
        nom_legende = fileName[len(fileName) - 1]
        pyplot.plot(listeEffectifs, label=nom_legende)

    # Ajout de la légende
    pyplot.legend()
    pyplot.title("Une magnifique Courbe")
    pyplot.xlabel("Longueur des Mots")
    pyplot.ylabel("Fréquence")

    # Save du file et affichage
    pyplot.savefig("frequences_V3.png")
    pyplot.show()


# On récupère les data
textArray = getTextPathMultiDir(textsFolder)

# On affiche avec la fonction faite précédemment
print(" ----- Affichage avec la fonction de base ----- ")
DistribMotSelonTailleV2(textArray)

print("\n\n ===== ----- ===== \n\n")

# On affiche avec la fonction modfié
print(" ----- Affichage avec la fonction modifier (set()) -----")
DistribMotSelonTailleV3(textArray)

"""## Exercice Bonus"""

print("\n\n ===== -- After Install -- ===== \n\n")

phrase = "L’élision est l’effacement d’une voyelle enfin de mot devant la voyelle commençant le mot suivant."

print(phrase.split())

tokenize = MosesTokenizer(lang='fr')
mots = tokenize(phrase)
tokenize.close()
print(mots)


def DistribMotSelonTailleV4(listFiles):
    listlang_word = {}
    listlang_nbrCharByWord = {}

    for fileItem in listFiles:
        # Lecture
        fileRead = open(fileItem)
        chaine = fileRead.read()
        fileRead.close()

        # Evolution du code du prof (J'avais un bug lors du split)
        #fileName = fileItem.split("/")
        #nom_legende = fileName[len(fileName) - 1]  # On prend le dernier element du tableau donc le nom
        # En supposant que le format soit toujours langFormat (fr, it, ..) + _ + autre
        #langue = nom_legende.split('_')[0]

        fileName = fileItem.split("/")
        temp = []
        for item in fileName:
          temp.extend(item.split("\\"))
        fileName = temp
        nom_legende = fileName[len(fileName) - 1]  # On prend le dernier element du
        langue = nom_legende.split('_')[0]

        print(langue)

        # Split
        # listMot = chaine.split()
        # listMot = set(listMot)

        # https://github.com/moses-smt/mosesdecoder/tree/master/scripts/share/nonbreaking_prefixes
        # Langues supportées par le tokenize
        langSupport = ["as", "bn", "ca", "cs", "de", "el", "en", "es", "et", "fi", "fr", "ga", "gu", "hi", "hu", "is",
                       "it", "kn", "lt", "lv", "ml", "mni", "mr", "nl", "or", "pa", "pl", "pt", "ro", "ru", "sk", "sl",
                       "sv", "ta", "te", "yue", "zh"]

        phrase = chaine.split()

        if langue in langSupport:
            try:
                tokenize = MosesTokenizer(langue)
                listMot = tokenize(chaine.replace("\n", ""))
                # print("Tokenize work ! for "+langue)
                tokenize.close()
            except:
                # print("Tokenize doesnt work ! for "+langue)
                listMot = phrase
        else:
            listMot = phrase
        # print(langue)
        # print("=====")
        # print(len(listMot))
        # listlang_word.append([langue, len(listMot)])
        # print(langue+ " : "+str(len(listMot)))
        if langue in listlang_word.keys():
            existValue = listlang_word[langue]
            updateValue = existValue + len(listMot)
            listlang_word[langue] = updateValue
        else:
            listlang_word[langue] = len(listMot)

        subDictnbrChar_occur = {}
        for word in listMot:
            nbrChar = len(word)
            if nbrChar in subDictnbrChar_occur.keys():
                subDictnbrChar_occur[nbrChar] = subDictnbrChar_occur[nbrChar] + 1
            else:
                subDictnbrChar_occur[nbrChar] = 1

        if langue in listlang_nbrCharByWord.keys():
            exist = listlang_nbrCharByWord[langue]
            for item in subDictnbrChar_occur.keys():
                if item in exist.keys():
                    exist[item] = exist[item] + subDictnbrChar_occur[item]
                else:
                    exist[item] = subDictnbrChar_occur[item]

            listlang_nbrCharByWord[langue] = exist
        else:
            listlang_nbrCharByWord[langue] = subDictnbrChar_occur

        # Dictionnaire
        dicLongueurs = setDicLongueur(listMot)

        listeEffectifs = []
        for toto in range(30):
            if toto in dicLongueurs:
                listeEffectifs.append(dicLongueurs[toto])
            else:
                listeEffectifs.append(0)

        # pyplot.plot(listeEffectifs)
        # nom_legende= fileItem

        pyplot.plot(listeEffectifs, label=nom_legende)

    # print(listlang_word)
    print("Nombre de mot :")
    for key in listlang_word.keys():
        print(key + " => " + str(listlang_word[key]) + "mots")

    print("\n\n Nombre de mots avec X caractères ( nombreDeCaractere => nombreDeMot) :")
    # print(listlang_nbrCharByWord)
    for key in listlang_nbrCharByWord.keys():
        print("\nPour le pays : " + key)
        print("================================")
        listItems = listlang_nbrCharByWord[key]
        for item in listItems.keys():
            print("Mot de " + str(item) + " caractères => " + str(listItems[item]) + " occurences - Soit : " + str(
                round((listItems[item] / listlang_word[key] * 100), 2)) + "%")

    print("\n\n ===== -- Show Figure -- ===== \n\n")

    # Ajout de la légende
    pyplot.legend()
    pyplot.title("Une magnifique Courbe")
    pyplot.xlabel("Longueur des Mots")
    pyplot.ylabel("Fréquence")

    # Save du file et affichage
    pyplot.savefig("frequences_V4.png")
    pyplot.show()


# Execution
DistribMotSelonTailleV4(textArray)