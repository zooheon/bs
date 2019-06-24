import re

list1=[]
def filelist():
     f=open("C:\croll\google.txt","r",encoding="utf-8")
     data=f.read()
     list1=data.split('\n')
     return list1


def search(datalist):
    re1='((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*))'	# HTTP URL 1
    re2='((?:[a-z][a-z\\.\\d\\-]+)\\.(?:[a-z][a-z\\-]+))(?![\\w\\.])'
    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    for i in datalist:
        txt=i
        m = rg.search(txt)
        httpurl1=m.group(1)
        fqdn1=m.group(2)
        list1.append(httpurl1+fqdn1)

        
def writeANDdelete(list):
     list1.sort()
     i=0
     f=open("C:\croll\googletest.txt",'a',encoding='UTF8')
     while(i<(len(list1)-1)):
          if(list1[i] in list1[i+1]):
               del list1[i+1]
          f.write(list1[i]+"\n")
          print(list1[i])
          i=i+1
     
     
a=filelist()
search(a)
writeANDdelete(list1)


