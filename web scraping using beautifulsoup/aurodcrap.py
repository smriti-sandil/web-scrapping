from autoscraper import AutoScraper
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path="C:\Program Files (x86)\chromedriver.exe"
# driver=webdriver.Chrome(path)
url=f'https://www.shein.co.uk/Men-Tops-c-1970.html?ici=CCCSN=MenHomePage_ON=Banner_OI=1_CN=Category_TI=50001_aod=0_PS=HZ-5-1_ABT=0&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~&srctype=homepage&userpath=%3EMenHomePage%3EMen-Tops'
scraper=AutoScraper()
category=f"https://www.shein.co.uk/Men-Striped-Trim-Polo-Shirt-p-1396691-cat-1981.html?scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~"
result=scraper.build(url,category)

print(result)