#!/usr/bin/env python3

#retrieve methods for file download
import yDownloader
import sys

def main():
    args = sys.argv[1:]

    print("On entre dans le programme python pour la récupération des titres de vidéos...\n")

    if(len(args) == 0):
        print("il n'y a aucun titre à récupérer : arrêt ")
        return
    
    print("Les titres à récupérer sont associés aux liens suivants : \n "+str(args))

    yDownloader.startSave(args)
   

if __name__ == "__main__":
    main()