# -*- coding: utf-8 -*-
import os
import codecs
from datetime import datetime
import requests
import HTML_DOWNLOADER as down
import DeQuirk as DQ


DIRECTORY_NAME = "pages"
DIRECTORY_NAME2 = "pages_as_non-HTML"
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
INPUT_DIR = DIR_PATH + "\pages_as_non-HTML"
OUTPUT_DIR = DIR_PATH + "\dequirked_files"
PAGE_COUNT = int(requests.get("https://api.deconreconstruction.com/pages/count?story.name=vast-error&published_at_null=false").content)#-227

down.download(PAGE_COUNT)
if (os.path.isdir("dequirked_files") == False):
        os.mkdir("dequirked_files")
        print(f"Directory 'dequirked_files' created successfully.")
start = datetime.now()
for i in range(2, PAGE_COUNT + 1):
    try:
        with open(f"{INPUT_DIR}\{i}.txt", "r", encoding = "utf-8") as page:
            of = open(f"{OUTPUT_DIR}\{i}-dequirked.txt", "w", encoding = "utf-8")
            for line in page:
                line.rstrip("\n")
                newLine = DQ.DeQuirk(line)
                newLine = DQ.deSlashify(newLine)
                newLine = newLine.rstrip("\n")
                of.write(newLine + "\n")
                page.close
                of.close
        print(f"page {i} added")
    except FileNotFoundError:
        print(f"page {i} not found")
delta = (datetime.now()-start).total_seconds()
print(f"Dequirked {PAGE_COUNT} pages in {delta} s")
print(f"Pages stored in '{OUTPUT_DIR}'.")



