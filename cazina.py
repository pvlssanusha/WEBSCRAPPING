import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
url='https://cazina.in/collections/kurti'
respomse=requests.get(url)
result=BeautifulSoup(respomse.text,"html.parser")
s=result.find_all('s')
p=result.find_all('span',attrs="price-item price-item--sale price-item--last")
name=result.find_all('a',attrs="full-unstyled-link")
Names=[]
for i in range(len(name)):
    if(i%2==0):
        e=name[i].text.split("\n")
        Names.append(e[1])
list2=[]
for i in p:
    sp=i.text.split(" ")
    w=sp[9].split("\n")
    list2.append(w[0])
list=[]
for i in s:
    sp=i.text.split("\n")
    p=sp[2].split(" ")
    list.append(p[-1])
finallist=[]
for i in range(len(list)):
    list3=[]
    list3.append(Names[i])
    list3.append(list[i])
    list3.append(list2[i])
    finallist.insert(i,list3)
table=PrettyTable(["ITEM NAME","ACTUAL PRIZE","OFFER PRIZE"])
for i in finallist:
    table.add_row(i)
print(table)