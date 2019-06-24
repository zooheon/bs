from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import re

f=open("C:\croll\google1.txt",'a',encoding='UTF8')
def googleex():
    f=open("C:\croll\googletest.txt","r",encoding="utf-8")
    data=f.read()
    list1=data.split('\n')
    String=""
    z=0
    while(z<len(list1)):
        String=String+" -"+list1[z]
        z=z+1
    return String
        
def google(url):
    for i in range(10):
        url1="https://www.google.co.kr/search?q=site%3A"+str(url)+"&num=100&start="+str(i*100)
        print(url1)
        r=requests.get(url1)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        link =soup.find_all("h3",{'class':'r'})
        href=re.compile("https://[\w]+[.]modoo[.]at/")
        for z in link:
            f.write(str(z))
            f.write("\n")
            print(z)

def today(a):
    google

string=googleex()
google("cafe24.com")
google("modoo.at")

