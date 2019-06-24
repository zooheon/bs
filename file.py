def findnew():
    f1=open("C:\croll\cityfood.txt")
    f2=open("C:\croll\cityfood1.txt")
    filecontext1=f1.read()
    data1=filecontext1.split("}{")
    lst=[]
    i=0
    j=0
    filecontext2=f2.read()
    data2=filecontext2.split("}{")
    while j<len(data2):
        if (data1[i]==data2[j]):
            i=i+1
            j=j+1
        else:
            lst.append(data2[j])
            j=j+1
            
    print(lst)

findnew()
