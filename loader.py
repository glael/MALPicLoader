#more34611{background-image: url(https://myanimelist.cdn-dena.com/images/anime/12/83498.jpg);}
# update by the magnificent TycoDJ / Project Tyco (weeb REEEEE)
import urllib.request
from bs4 import BeautifulSoup
import json

userName = "Glael" #your username
listType = "anime" #"anime" or "manga"

url = 'https://myanimelist.net/' + listType + 'list/' + userName
header = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}

mobileRequest = urllib.request.Request(url, headers=header)
resp = urllib.request.urlopen(mobileRequest)
page = resp.read()

soup = BeautifulSoup(page.decode('utf-8'), 'html.parser')

# the webpage contains all the data as a stringified json object
dataList = str(soup.find(id="app"))
dataList = dataList.replace("&quot;", "\"")	# idk this probably can be done with beautifulsoup but this works
dataList = dataList[16:-17]

dataList = json.loads(dataList)

items = dataList["items"]

for uwu in items:	# in python this just puts the current key (as string) in uwu, still have to call items[uwu] for value
	owo = items[uwu]	# final sub-dictionary which includes id & image path

	print("#more" + str(owo["id"]) + "{background-image: url(https://myanimelist.net" + owo["image"] + ");}")
