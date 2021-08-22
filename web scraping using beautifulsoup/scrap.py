from autoscraper import AutoScraper
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import zipfile
import gdown
url=f"https://drive.google.com/file/d/11sjldrLof_0x2MbOete24K_B8F-0APYz/view"
output='samples.zip'
gdown.download(url,output,quiet=False)
# r=requests.get(url)
# with open('data.zip','wb') as f:
#     f.write(r.content)

# with zipfile.ZipFile('data.zip','r') as f:
#     print(f.namelist())


# Read zip files from page, download file, extract and stream output
from io import BytesIO
from zipfile import ZipFile
import urllib.request
import os,sys,requests,csv
from bs4 import BeautifulSoup

# check for download directory existence; create if not there
if not os.path.isdir('dowload'):
    os.makedirs('dowload')

# Get labels and zip file download links
# mainurl = "http://www.test.com/"
# url = "http://www.test.com/thisapp/GetReports.do?Id=12331"

# get page and setup BeautifulSoup
# r = requests.get(url)
# soup = BeautifulSoup(r.content, "html.parser")
# print(soup.findAll('script')[6])
# # Get all file labels and filter so only use CSVs
# mainlabel = soup.find_all("td", {"class": "labelOptional_ind"})
# for td in mainlabel:
#     if "_csv" in td.text:
#         print(td.text)

# # Get all <a href> urls
# for link in soup.find_all('a'):
#     print(mainurl + link.get('href'))


from googleDriveFileDownloader import googleDriveFileDownloader as gd
a=gd()
a.downloadFile(url)