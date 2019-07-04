import codecs
import urllib, re
import requests
import urllib.request
import datetime
import lxml.html
import os
import time
from bs4 import BeautifulSoup

genre = "muralism"
style ="genre"

hard ="./Wiki_art_dataset/" + genre + "/"

if not os.path.exists(hard):
    os.makedirs(hard)

#xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )


url = "https://www.wikiart.org/en/paintings-by-"+style+"/"+genre
print(url)

html = lxml.html.parse(urllib.request.urlopen(url) )
links = [i.strip() for i in html.xpath("//ul[contains(@class, 'artists-group-list')]/li/a/@href")]

num = 0

for link in links:
    #print (link)
    split = "="

    name = link[link.index(split) + len(split):]
    final_link = "https://www.wikiart.org" + link

    img = urllib.request.urlopen(final_link).read()

    try:
        result = re.search('&quot;https://uploads(.*).wikiart.org/(.*).jpg', str(img) )
        result1 = re.search('&quot;https://uploads(.*).wikiart.org/(.*).JPG', str(img) )

        raw = result.group()
        raw1 = result.group()

        clean = raw.split("&quot;")
        clean1 = raw1.split("&quot;")

        for i in clean or i in clean1:
            try:
                if len(i) < 16:
                    continue
                else:
                    #print(i)
                    save_img = urllib.request.urlretrieve(i,hard+genre+"_"+name+"_"+str(num)+".jpg")
                    num +=1
            except:
                continue
    except:
        continue


print("That's All Folks!")
