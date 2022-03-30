from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import time

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input("검색할 태그를 입력하세요: ")
url = baseUrl + quote_plus(plusUrl) 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#wait for image fetching 
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, features='html.parser')

insta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1
for i in insta:
  print('https://www.instagram.com' + i.a["href"])
  imgUrl = i.select_one("img")['src']
  with urlopen(imgUrl) as f:
    with open("./img/" + plusUrl + str(n) + ".jpg", "wb") as h:
      img = f.read()
      h.write(img)
  
  n += 1
  print(imgUrl)
  print()

driver.close()