#!/usr/bin/env python3

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


#créer un fichier à inclure qui gère entièrement la transformation d'un fichier mp3 en fichier mp4 et ensuite appeler
# une méthode de ce fichier dans downloadMP3
# download MP3 appel downloadMP4 puis appel ce fichier à inclure sur le fichier puis supprime le fichier au format mp4
def downloadMP3(link, newTitleOn:bool=False, Mp3_outputPath:str="/home/nathanb/Bureau/Bureau/Bureau/Perso/projets_développement_informatique/VideoConverterPersonalFiles/MP3_output"):
    try:

        #from ytubefix official manual
        yt = YouTube(link, on_progress_callback = on_progress)
        newTitle = yt.title
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)

        #update du titre de l'audio si nécessaire
        if(newTitleOn):
            newTitle = updateFileTitle(yt.title+".mp3", ".mp3")
            print("titre mis à jour")

        #on garde l'ancien titre
        else:
            newTitle = newTitle+".mp3"
            print("on garde le titre par défaut")
        
        subprocess.call(["mv",newTitle,Mp3_outputPath])

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


def downloadMP4(link:str, newTitleOn:bool=False, pathForMp4output:str="/home/nathanb/Bureau/Bureau/Bureau/Perso/projets_développement_informatique/VideoConverterPersonalFiles/MP4_output"):
    youtubeObject = YouTube(link, on_progress_callback = on_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        #se déplace vers le dossier pour les fichiers MP4
        youtubeObject.download()
        print("Download MP4 is completed successfully \n")
        newTitle = youtubeObject.title
        print("Le titre de la vidéo MP4 est : "+newTitle)
        if(newTitleOn):
            newTitle = updateFileTitle(youtubeObject.title+".mp4", ".mp4")
            print("titre mis à jour")
        else:
            newTitle = newTitle+".mp4"
            print("on garde le titre par défaut")

        #déplace le fichier dans le bon dossier
            
        MP4_outputPath = pathForMp4output
        print("le new title est : "+newTitle+"\n\n")
        print("le dossier pour votre fichier MP4 EST : "+MP4_outputPath+"\n")
        #subprocess.call(["pwd"])
        subprocess.call(["mv",newTitle,MP4_outputPath])

        #on renvoie le nouveau titre du fichier sans le path
        return newTitle
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        traceback.print_tb(exception_traceback, limit=2, file=sys.stdout)
    


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
def startDownload(listeLiensVideos:list,newTitleOn:bool=False, choixFormatFichier:int=0):
    #go to project directory
    pathFileForProject = findFileWithPath("VideoConverter/python_script_download")


    mp3Path = findFileWithPath("VideoConverterPersonalFiles/MP3_output")
    mp4Path = findFileWithPath("VideoConverterPersonalFiles/MP4_output")
    #downloadMP4(fichier, newTitle, Mp3_outputPath:str="VideoConverterPersonalFiles/MP3_output",Mp4_outputPath:str="VideoConverterPersonalFiles/MP4_output")

    os.chdir(pathFileForProject)
    if(len(listeLiensVideos) == 0): #pas de vidéos à traiter
        return
    while(choixFormatFichier != 1 and choixFormatFichier != 2):
        choixFormatFichier = int(input("Voulez-vous convertir en un fichier mp3 (1) ou mp4 (2)? : \n"))

    if(choixFormatFichier == 2):
        print("Le dossier pour vos fichiers mp3 est : "+mp4Path)
        for fichier in listeLiensVideos:
            #print("les liens vidéos à traiter : "+el)
            downloadMP4(fichier, newTitleOn, mp4Path)

    elif(choixFormatFichier == 1):
        print("Le dossier pour vos fichiers mp3 est : "+mp3Path)
        for fichier in listeLiensVideos:
            #print("les liens vidéos à traiter : "+el)
            downloadMP3(fichier, newTitleOn, mp3Path)

#ajouter une fonctionnalité de mutli-threading pour permettre le multi-téléchargement et autoriser l'utilisation d'une liste 
#d'argument et montrer d'autres compétences
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("aucun fichier à télécharger : terminé ! \n")
        return
    newTitleOn = False

    print("il faut télécharger "+str(len(args))+" fichiers .\n")
    #On propose de choisir un nouveau titre, si il n'y a pas trop de fichiers à traiter
    #c'est à dire - de 4 

    if(len(args) <= 4):
        newTitleOn = newTitleChoice()

    startDownload(args, newTitleOn)

if __name__ == "__main__":
    main()