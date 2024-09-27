#!/usr/bin/env python3

import shlex
from pytube import YouTube
import subprocess
from moviepy.editor import *
import re
import sys
from io import StringIO # Python3 use: from io import StringIO
import sys
import traceback
import os



#code récupéré d'internet 
# référence:  https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/


#créer un fichier à inclure qui gère entièrement la transformation d'un fichier mp3 en fichier mp4 et ensuite appeler
# une méthode de ce fichier dans downloadMP3
# download MP3 appel downloadMP4 puis appel ce fichier à inclure sur le fichier puis supprime le fichier au format mp4
def DownloadMP3(link, newTitleOn:bool=False, Mp3_outputPath:str="MP3_output",Mp4_outputPath:str="MP4_output"):
    try:
        oldTitle = DownloadMP4(link, newTitleOn)

        #recupère la vidéo MP4 (BEGINNING)

        print("le titre du fichier MP4 est : "+oldTitle)

        #récupère le path vers le dossier des fichiers MP4
        MP4_outputPath = Mp4_outputPath
        

        #recupère la vidéo MP4
        videoMP4 = VideoFileClip(Mp4_outputPath+"/"+oldTitle)
        #renomme l'ancient titre avec son titre version mp3
        newTitle = oldTitle.replace(".mp4", ".mp3")


        #récupère le path vers le dossier des fichiers MP3

        MP3_outputPath = Mp3_outputPath

        #recupère la vidéo MP4 (ENDING)

        #converti l'audio MP4 en mp3 avec son path et son nouveau titre
        videoMP4.audio.write_audiofile(MP3_outputPath+"/"+newTitle)
        
        #supprime la version mp4 qui est inutile
        subprocess.call(["rm",MP4_outputPath+"/"+oldTitle])
        return newTitle

    except Exception as error_message:
        print(error_message)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        traceback.print_tb(exception_traceback, limit=2, file=sys.stdout)


#utiliser les commandes terminales pour changer le titre de la vidéo
#renvoie le nouveau titre
def updateFileTitle(fileName: str):
    newTitle = ""
    while(newTitle == "" or len(newTitle) > 100):
        print("L'ancien titre du fichier est : "+fileName+"\n")
        newTitle = input("Donnez le nouveau titre du fichier(max 100 caractères pour éviter les scripts) :  \n")

    #update du nom
    subprocess.call(["mv",fileName,newTitle+".mp4"])
    return newTitle+".mp4"
            
    



def findFileWithPath(pathBegin:str):
    #\*YtubeDonwloader/python_script_download/MP3_output
    strForSubProcess = "find ~ -path \\*"+ pathBegin +" -print -quit"
    #subprocess.call("find ~ -path \*YtubeDonwloader/python_script_download/MP3_output -print -quit", shell=True)
    subprocess.call(strForSubProcess, shell=True)
    #il faut trouver un moyen de récupérer la sortie standard dans une variable... pour récupérer le path qui est donné
    pathSearchedInBytes = subprocess.check_output(strForSubProcess, shell=True)
    actualStr = pathSearchedInBytes.decode('ASCII').rstrip()
    return actualStr


def DownloadMP4(link:str, newTitleOn:bool=False, pathForMp4output:str="MP4_output"):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        #se déplace vers le dossier pour les fichiers MP4
        youtubeObject.download()
        print("Download MP4 is completed successfully \n")
        newTitle = youtubeObject.title
        print("Le titre de la vidéo MP4 est : "+newTitle)
        if(newTitleOn):
            newTitle = updateFileTitle(youtubeObject.title+".mp4")
            print("titre mis à jour")
        else:
            newTitle = newTitle+".mp4"
            print("on garde le titre par défaut")

        #déplace le fichier dans le bon dossier
            
        MP4_outputPath = pathForMp4output
        print("le new title est : "+newTitle+"\n\n")
        print("le dossier pour MP4 EST : "+MP4_outputPath+"\n")
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
    pathFileForProject = findFileWithPath("YtubeDownloader/python_script_download")
    os.chdir(pathFileForProject)
    if(len(listeLiensVideos) == 0): #pas de vidéos à traiter
        return
    while(choixFormatFichier != 1 and choixFormatFichier != 2):
        choixFormatFichier = int(input("Voulez-vous convertir en un fichier mp3 (1) ou mp4 (2)? : \n"))

    if(choixFormatFichier == 2):
        for fichier in listeLiensVideos:
            #print("les liens vidéos à traiter : "+el)
            DownloadMP4(fichier, newTitleOn)

    elif(choixFormatFichier == 1):
        for fichier in listeLiensVideos:
            #print("les liens vidéos à traiter : "+el)
            DownloadMP3(fichier, newTitleOn)

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