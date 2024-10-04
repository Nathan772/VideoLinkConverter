#!/usr/bin/env python3

#retrieve methods for file download
import yDownloader
import sys

def main():
    args = sys.argv[1:]

    print("On entre dans le programme python pour le download...\n")

    if(len(args) == 0):
        print("il n'y a aucun fichier à télécharger : arrêt ")
        return
    
    print("Les fichiers à télécharger sont associés aux liens suivants : \n "+str(args))

    yDownloader.startDownload(args, False, 1)
   

if __name__ == "__main__":
    main()