#from Issam Hz nikname @Zitssu 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import time 
import numpy as np
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"')
chrome_options.add_argument("--user-data-dir=C:/Users/pc/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(chrome_options=chrome_options , executable_path="D:/chromedriver/chromedriver.exe")

#print in file and remove the wrong trades or messages
def remove_x(messages):
    if "SL" in messages:
                if "Tp" or "TP" in messages:
                    if "PIPS" and "pip" not in messages:
                        f = open(r"D:/code/test.txt", "a")
                        print("Found = " + messages + "\n" )
                        f.write("Found = " + messages + "\n" +"----------------------------------------------------------------------------------" +"\n" )
                        f.close()

#def for data
def get_data(url):
    driver.get(url)
    driver.refresh()
    time.sleep(8)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,"lxml")
    msg = soup.find_all('div' , class_="message-date-group")
    for content in msg[-1]:
        for data in content.find_all("p"):
            messages = data
            #data.find('span' , class_='message-time').decompose()
            #data.find('span' , class_='message-views').decompose()
            #print(messages.text + "\n" )
            messages = messages.get_text(separator=" ").strip()
            remove_x(messages)

#end
#driver.quit()

#'p' class text-content with-meta
#'div' "message168463" Message message-list-item first-in-group last-in-group has-views open shown 
#'div' "date"  message-date-group
#'div' the main  messages-container
#'button' the buton for the news messages  =  Button sgkkv3bmIMAZS9G9BHUz default secondary round

#goups on telegram webs id 
groups = ['1237603036','1422733304','1284268486','1235677912','1671271638',
          '1471999753','1415396489','1484511130','1354540851','1145980603',
          '1751966248','1175655190','1605563972','1365880004','1302401641',
          '1343510333','1551322160','1311425945','1423626269',]

for i in range(len(groups)):
    x = groups[i]
    url  = "https://web.telegram.org/z/#-" + x
    print(url)
    get_data(url)

#,'1425350180'
#html = html.replace("<br>", " ")
#title = title_box.get_text(separator=" ").strip()
