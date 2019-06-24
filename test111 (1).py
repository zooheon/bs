from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from datetime import datetime

def switch():
    f1=open("C:\croll\cityfood.txt")
    f2=open("C:\croll\cityfood1.txt")
    filecontext1=str(f1.read())
    filecontext2=str(f2.read())
    f1.close
    f2.close
    f1=open("C:\croll\cityfood.txt",'w')
    f2=open("C:\croll\cityfood1.txt",'w')
    f1.write(filecontext2)

def findnew():
    f1=open("C:\croll\cityfood.txt")
    f2=open("C:\croll\cityfood1.txt")
    filecontext1=f1.read()
    data1=filecontext1.split("}{")
    filecontext2=f2.read()
    data2=filecontext2.split("}{")
    pre=list(set(data1)-set(data2))
    pro=list(set(data2)-set(data1))
    
    s=str(datetime.today().year)+str(datetime.today().month)+str(datetime.today().day)
    k="C:\croll\cityfood"+s+".txt"
    f3=open(k,'w')
    print(pre)
    print(pro)


def cityfood(url):
    f=open("C:\croll\cityfood1.txt",'a')
    
    for k in range(1, 2):
        try:
            url1=url+str(k)+"&word="
            html = urlopen(url1).read()
            soup = BeautifulSoup(html, "html.parser")
            for i in range(5):
                korean_food = {}
                data_set = soup.select('div.search-list  li.context')[i].text
                data_split = data_set.split('\n')
                key_escape = data_split[2]
                key = re.sub(r'\t', '', key_escape).strip()
                if key=="서가수제돈까스":
                    continue
                value = data_split[-3].strip()
                korean_food[key] = value
                context=str(korean_food)
                f.write(context)
        except:
            f.close()
            break
findnew()
a=input("종료하려면 아무키나 누르싶시오")
