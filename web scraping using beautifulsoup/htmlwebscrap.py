# # from requests_html import HTMLSession
# # url="https://internshala.com/internships/"
# # s=HTMLSession()
# # r=s.get(url)
# # r.html.render(sleep=1)
# # i=0
# # Intern=r.html.xpath('//*[@id="internship_list_container"]',first=True)
# # for item in Intern.absolute_links:
# #     r=s.get(item)
# #     Intern_name=r.html.find('div.heading_4_5.profile',first=True)
# #     Intern_name=Intern_name.text
# #     print(Intern_name)
# #     i+=1
# # print(i)


# # import requests
# # from bs4 import BeautifulSoup
# # url='https://internshala.com/internships'
# # r=requests.get(url)
# # soup=BeautifulSoup(r.content,'html.parser')
# # print(soup.title.text)
# # Intern_name=soup.find('a',class_='heading_4_5.profile').text.strip()
# # Intern_Type=soup.find('div',class_='label_container label_container_desktop').text.strip()
# # print(Intern_name,Intern_Type)


# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# baseurl="https://internshala.com/"
# headers={
#     'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
# }

# r= requests.get("https://internshala.com/internships")
# soup=BeautifulSoup(r.content,'lxml')

# Inter_list=soup.find_all('div',class_='container-fluid individual_internship')
# # print(Inter_list)
# Intern_link=[]
# for item in Inter_list:
#     for link in item.find_all('a',class_='view_detail_button',href=True):
#         Intern_link.append(baseurl+link['href'])
#         # print(link['href'])

# # print(Intern_link)
# I_l=[]
# l=''
# # testlink='https://internshala.com/internship/details/covid-emergency-langar-sewa-delivery-assistance-part-time-job-internship-at-noida-in-proof-of-performance-data-services-private-limited1620118753'
# for link in Intern_link:
#     if l!=link:
#         r=requests.get(link,headers=headers)
#         soup=BeautifulSoup(r.content,'lxml')
#         Intern_name=soup.find('div',class_='heading_4_5 profile').text.strip()
#         Comp_name=soup.find('a',class_='link_display_like_text').text.strip()
#         Location=soup.find('a',class_='location_link').text.strip()
#         Intern_Type=soup.find('div',class_='label_container label_container_desktop').text.strip()
       
#         try:
#             Start=soup.find('span',class_='start_immediately_desktop').text.strip()
#         except:
#             Start="Immediately"
        
#         Stpend=soup.find('span',class_='stipend').text.strip()
#         Internship={
#             'Intern_name':Intern_name,
#             'Company_name': Comp_name,
#             'Location': Location,
#             'Start date': Start,
#             'Stpend': Stpend,
#             'Intern_Type': Intern_Type,
            
#         }
#         I_l.append(Internship)
#         print('saving:',Comp_name)
#     else:
#         pass
#     l=link
#     # print(Internship)
# # print(Inter_list)
# df=pd.DataFrame(I_l)
# print(df.head(30))


import re
from bs4.element import NavigableString
import requests
import pandas as pd
from bs4 import BeautifulSoup





url=f'https://www.shein.co.uk/Men-Tops-c-1970.html?ici=CCCSN=MenHomePage_ON=Banner_OI=1_CN=Category_TI=50001_aod=0_PS=HZ-5-1_ABT=0&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~&srctype=homepage&userpath=%3EMenHomePage%3EMen-Tops'
headers={
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
r=requests.get(url,headers)
soup=BeautifulSoup(r.content,'html.parser')
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# d=soup.find_all(has_class_but_no_id)
# print(d)

data=soup.find_all('div',class_="S-product-item__wrapper")
print(data)
