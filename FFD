import requests, sys, os, wget, re
from bs4 import BeautifulSoup

os.system('clear')

for i in range(0, 9):
    os.system('clear')
    w_path = 'img/'

    url_ = input("URL: ")
    req = requests.get(url_)
    soup = BeautifulSoup(req.text, "lxml")
    print(soup.img['src'])

    outF = open("list", "w")
    for all in soup.find_all('img', recursive=True, attrs={'src': re.compile("^http://")}):
        image = all.get("src")
        outF.write(image+"\n")
        req
    outF.close()

    f = open("list", "r")
    lines = f.readlines()
    for line in lines:
        wget.download(str(line), out="img/")
