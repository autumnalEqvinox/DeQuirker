# -*- coding: utf-8 -*-
import os
import codecs
from datetime import datetime
import requests
import HTML_DOWNLOADER as down
import DeQuirk as DQ
from bs4 import BeautifulSoup
from pathlib import Path

# saving a bunch of global variables
directory_name = "pages"
directory_name2 = "pages_as_non-HTML"
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path + "\\pages_as_non-HTML"
output_path = dir_path + "\\dequirked_files"
page_count = int(requests.get("https://api.deconreconstruction.com/pages/count?story.name=vast-error&published_at_null=false").content)#-227
comp_count = 0

#fchecks the "count.txt" file, if it exists, it reads the first line to store the last saved page_count
p = Path(f'{dir_path}\\page_count.txt')
try:
    with open("page_count.txt", "r") as file:
            comp_count = file.readline()
except FileNotFoundError:
        pass

# checks if either the stored page count in "count.txt" is less than the current page count OR if "page_count.txt" doesn't exist (i.e. first run of the program)
# makes the "pages_as_non-HTML" directory then converts that content into txt files using the beautifulsoup4 library and stores it in the created directory
if(int(comp_count) != page_count or p.exists != True):
    print("Downloading new files...")
    down.download(page_count)

    # if "pages_as_non-HTML" doesn't exist, make the directory
    if (os.path.isdir(directory_name2) == False):
        os.mkdir(directory_name2)
        print(f"Directory '{directory_name2}' created successfully.")
    if (os.path.isdir("pages_as_non-HTML") == True):
        for i in range(int(comp_count), page_count +1):
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
        with open("page_count.txt", "w") as file:
            file.write(str(page_count))
    file.close

# makes the "dequirked files" folder if it doesn't exist
if (os.path.isdir("dequirked_files") == False):
        os.mkdir("dequirked_files")
        print(f"Directory 'dequirked_files' created successfully.")

# used for timing the runtime
start = datetime.now()

# goes through ever file inside "pages_as_non-HTML"
for i in range(2, page_count + 1):
    try:

        # opens the current page
        with open(f"{dir_path}\\pages_as_non-HTML\\{i}.txt", "r", encoding = "utf-8") as page:

            # creates thes dequired output file for the current page
            of = open(f"{output_path}\\{i}-dequirked.txt", "w", encoding = "utf-8")

            # goes through every line inside the page
            for line in page:

                # gets ride of any new line characters to stop from bugs inside the dequirking function
                line.rstrip("\n")

                # takes the line and runs the dequirk function in DeQuirk.py
                newLine = DQ.DeQuirk(line)

                # deslashify gets rid of '\' chracters that appear in front of commas
                newLine = DQ.deSlashify(newLine)

                #write the line to a new file with a new line character at the end
                of.write(newLine + "\n")

                # close the page and output file
                page.close
                of.close

        # confirm whether or not page was added
        print(f"page {i} added")
    except FileNotFoundError:
        print(f"page {i} not found")

# gets runtime
delta = (datetime.now()-start).total_seconds()

# prints information
print(f"Dequirked {page_count} pages in {delta} s")
print(f"Pages stored in '{output_path}'.")

# wait for user input to close the program
os.system('pause')



