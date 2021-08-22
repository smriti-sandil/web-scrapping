
# from typing import Container
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen 
# url= "https://internshala.com/internships/"
# r=urlopen(url)
# page_html=r.read()
# r.close()

# page_soup=soup(page_html,'html.parser')

# cont=page_soup.find_all("div", {"class":"internship_list_container","id":"internship_list_container"})
# # print(len(cont))
# # print(soup.prettify(cont[0]))
# co=cont[0]
# "Intern_name"
# Intern_name=co.find_all("div",{"class":"heading_4_5 profile"})
# # print(Intern_name[0].text)
# "Intern link"
# # print(co.div.a["href"]) #Internlink
# "Intern Org_NAme"
# Intern_org_name=co.find_all("div",{"class":"heading_6 company_name"})
# # print(Intern_org_name[0].text)
# # Org_link=co.find('a')
# # print(Org_link["href"])

# # loc=co.find_all("div",{"id":"location_names"})
# # print(loc[0].text)

# # Start=co.find_all("span",{"class":"start_immediately_desktop"})
# # print(Start[0].text)

# dur=co.find_all("div",{"class":"item_body"})
# print(dur[0].text)

# import time
# from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# path="C:\Program Files (x86)\chromedriver.exe"
# driver=webdriver.Chrome(path)

# driver.get("https://internshala.com/internships/")
# # driver.get("https://www.adda247.com/")

# plink=driver.find_element_by_id("close_popup")
# plink.click()

# link=driver.find_element_by_id("navigation-forward")
# link.click()
# print(driver.title)
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "internship_list_container_1"))
#     )
#     print(main.text)
# except:
#     driver.quit()

# print(driver.page_source)
# main=driver.find_element_by_id("internship_list_container")

# # print(main.text)
# driver.quit()













import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://internshala.com/internships/")


plink=driver.find_element_by_id("close_popup")
plink.click()

# ele=driver.find_element_by_xpath('//*[@id="list_container"]')
# print(ele.text)

l=driver.find_elements_by_class_name("list_container")
print(l)
# driver.quit()
# link=driver.find_element_by_id("navigation-forward")
# link.click()
























