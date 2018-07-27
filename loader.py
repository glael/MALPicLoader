#more34611{background-image: url(https://myanimelist.cdn-dena.com/images/anime/12/83498.jpg);}

import urllib.request
from bs4 import BeautifulSoup

userName = "Glael" #your username
listType = "manga" #"anime" or "manga"


page = urllib.request.urlopen('https://myanimelist.net/' + listType + 'list/Glael')
soup = BeautifulSoup(page.read().decode("utf-8"),  "html.parser")

wow = soup.find_all("a", {"class": "animetitle"})

for i in wow:
    href = i.get("href")
    #print(href)

    animeNumber = i.get("href").split("/")[2]
    #print(animeNumber)

    animePageRequest = urllib.request.urlopen('https://myanimelist.net/' + listType + '/' + str(animeNumber))
    animePageSoup = BeautifulSoup(animePageRequest.read().decode("utf-8"),  "html.parser")


    imageUrl = animePageSoup.find("img", {"class": "ac", "itemprop": "image"}).get("src")
    #print(imageUrl)

    #print("######################################################################################################################################")

    print("#more" + str(animeNumber) + "{background-image: url(" + imageUrl + ");}")
