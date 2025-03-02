# -*- coding: utf-8 -*-
import os
import codecs
from datetime import datetime
import requests
import HTML_DOWNLOADER as down
import DeQuirk as DQ
from bs4 import BeautifulSoup


directory_name = "pages"
directory_name2 = "pages_as_non-HTML"
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path + "\\pages_as_non-HTML"
output_path = dir_path + "\\dequirked_files"
page_count = int(requests.get("https://api.deconreconstruction.com/pages/count?story.name=vast-error&published_at_null=false").content)#-227

down.download(page_count)
if (os.path.isdir(directory_name2) == False):
        os.mkdir(directory_name2)
        print(f"Directory '{directory_name2}' created successfully.")

if (os.path.isdir("pages_as_non-HTML")):
    for i in range(2, page_count +1):
        try:
            with open(f"{dir_path}\\pages\\{i}.html", "r") as page:
                soup = BeautifulSoup(page.read(), "html.parser")
                for br in soup.select("br"):
                    br.replace_with("\n")
                content = soup.find(id="content").get_text()
            with open(f"{input_path}\\{i}.txt", "w", encoding = "utf-8") as output:
                output.write(content)

            print(f"page {i} added")
        except FileNotFoundError:
            print(f"page {i} not found")

if (os.path.isdir("dequirked_files") == False):
        os.mkdir("dequirked_files")
        print(f"Directory 'dequirked_files' created successfully.")
start = datetime.now()
for i in range(2, page_count + 1):
    try:
        with open(f"{dir_path}\\dequirked-pages\\{i}.txt", "r", encoding = "utf-8") as page:
            of = open(f"{output_path}\{i}-dequirked.txt", "w", encoding = "utf-8")
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
print(f"Dequirked {page_count} pages in {delta} s")
print(f"Pages stored in '{output_path}'.")
os.system('pause')



