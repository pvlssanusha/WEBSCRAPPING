from selenium import webdriver
from time import sleep
path = 'C:\chromedriver.exe'
# open the browser
browser = webdriver.Chrome(executable_path=path)
# load the webpage
browser.get('https://www.amazon.in/Samsung-Galaxy-Storage-MediaTek-Battery/dp/B0BMGB2TPR/ref=sr_1_1?crid=449D3903U128&keywords=samsung%2Bj8&qid=1674227056&sprefix=samsung%2Bj8%2Caps%2C256&sr=8-1&th=1')
browser.maximize_window()
from bs4 import BeautifulSoup
soap=BeautifulSoup(browser.page_source,'html.parser')
soap
list=[]
for x in soap.find_all('i'):
    y=x.find('span',attrs="a-icon-alt")
    if y is not None:
            if "out" in y.text:
                list.append(y.text)
list
list2=[]
for x in soap.find_all('div',attrs="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
    y=x.find('span')
    if y is not None:
        list2.append(y.text)
print("The Ratings  are")
print(list)
print("\nThe Reviews are :")
print(list2)

        
