#!/usr/bin/env python3

#retrieve methods for file download
import yDownloader
import sys

def main():
    args = sys.argv[1:]
    print("le contenu de args est : "+str(args))
    yDownloader.startDownload(args, False, 1)
   

if __name__ == "__main__":
    main()