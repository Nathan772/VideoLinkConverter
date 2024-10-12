#!/usr/bin/env python3


"""

Il faudrait ajouter du multi-threading pour compléter et rendre ça plus pertinent

"""


import shlex
#from pytube import YouTube
import subprocess
from moviepy.editor import *
import re
import sys
from io import StringIO # Python3 use: from io import StringIO
import sys
import traceback
import os

#remplacement pour pytube
from pytubefix import YouTube 
from pytubefix.cli import on_progress


#code récupéré d'internet 
# référence:  https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/


"""
Cette méthode permet de récupérer le titre de la vidéo que vous souhaitez
ajouter à votre historique de fichier mp3 youtube.
"""
def historiqueVideo(link):
    try:

        #from ytubefix official manual
        yt = YouTube(link, on_progress_callback = on_progress)
        newTitle = yt.title

        #on renvoie le nouveau titre du fichier sans le path
        return newTitle

    except Exception as error_message:
        print(error_message)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        traceback.print_tb(exception_traceback, limit=2, file=sys.stdout)


#utiliser les commandes terminales pour changer le titre de la vidéo
#renvoie le nouveau titre
def updateFileTitle(fileName: str, extension:str=".mp3"):
    newTitle = ""
    while(newTitle == "" or len(newTitle) > 100):
        print("L'ancien titre du fichier est : "+fileName+"\n")
        newTitle = input("Donnez le nouveau titre du fichier(max 100 caractères pour éviter les scripts) :  \n")

    #update du nom
    subprocess.call(["mv",fileName,newTitle+extension])
    return newTitle+extension
            
    



def findFileWithPath(pathBegin:str):
    #\*YtubeDonwloader/python_script_download/MP3_output
    strForSubProcess = "find ~ -path \\*"+ pathBegin +" -print -quit"
    #subprocess.call("find ~ -path \*YtubeDonwloader/python_script_download/MP3_output -print -quit", shell=True)
    subprocess.call(strForSubProcess, shell=True)
    #récupère la chaine renvoyée à la sortie standard en vraie chaine
    pathSearchedInBytes = subprocess.check_output(strForSubProcess, shell=True)
    actualStrForPath = pathSearchedInBytes.decode('utf-8').rstrip()
    #print("le path est : "+actualStrForPath)
    return actualStrForPath
    


def newTitleChoice():
    newTitleChoice = input("voulez-vous choisir un nouveau titre pour les fichiers ?, 2 (oui), 1 (non) \n")
    try:
        newTitleChoice = int(newTitleChoice)
        #the user want to choose a new name for the file
        if(newTitleChoice == 2):
            print("D'accord, on vous proposera de choisir le titre \n")
            return True
        #the user keep the same name
        else:
            return False
    #pas un nombre : on considère comme un "non"
    except ValueError:
        print("Vous avez choisi une lettre, cela sera perçu comme un 'non' \n")
        pass

    return False

#cette méthode démarre le téléchargement des fichiers en demandant 
#à l'utilisateur son choix de format
def startSave(listeLiensVideos:list):
    #go to project directory
    pathFileForProject = findFileWithPath("VideoConverter/python_script_download")
    #mp3Path = findFileWithPath("VideoConverterPersonalFiles/MP3_output")
    #mp4Path = findFileWithPath("VideoConverterPersonalFiles/MP4_output")
    #this value has to match with the number chosen in the java file VideoParsing.java in "retrieveVideoFileName"
    #otherwise it will cause trouble while parsing in the java file
    maxLinkFileSize = 400

    #journal des vidéos pour le java
    journal_de_bord_path_file = findFileWithPath("VideoConverter/outputfiles/journal_de_bord.txt")
    
    file_journal = open(journal_de_bord_path_file, "a")

    os.chdir(pathFileForProject)
    if(len(listeLiensVideos) == 0): #pas de vidéos à traiter
        return
    # while(choixFormatFichier != 1 and choixFormatFichier != 2):
    #     choixFormatFichier = int(input("Voulez-vous convertir en un fichier mp3 (1) ou mp4 (2)? : \n"))


    for lienVideo in listeLiensVideos:
        #print("les liens vidéos à traiter : "+el)
        nom_output_file = historiqueVideo(lienVideo)
        #ajoute le fichier dans le journal de bord pour java
        #il y a aussi du padding au cas où le nom de la vidéo est trop long (typiquement les vidéos japonaises)
        #la taille du lien youtube + nom vidéo doit être <= 400
        file_journal.write(lienVideo+"::"+nom_output_file+(maxLinkFileSize-(len(lienVideo)+len(nom_output_file)+3))*"*"+";\n")


    #fermeture du journal
    file_journal.close()


#ajouter une fonctionnalité de mutli-threading pour permettre le multi-téléchargement et autoriser l'utilisation d'une liste 
#d'argument et montrer d'autres compétences
def main(argv):
    args = argv
    for el in args:
        print(el)
    if len(args) == 0:
        print("aucune vidéo à récupérer : terminé ! \n")
        return

    print("il faut récupérer "+str(len(args))+" liens vidéos .\n")
    
    startSave(args)

"""
remarque : ne fonctionne pas lorsqu'on prend une vidéo directement depuis une playlist, à cause du fameux
"&index=..."
le "&" doit poser problème et être perçu comme une addition de commande.
"""
if __name__ == "__main__":
    main(sys.argv[1:])