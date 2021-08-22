import requests
from bs4 import BeautifulSoup
import pandas as pd
baseurl="https://internshala.com/"
headers={
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

r= requests.get("https://internshala.com/internships")
soup=BeautifulSoup(r.content,'lxml')

Inter_list=soup.find_all('div',class_='container-fluid individual_internship')
# print(Inter_list)
Intern_link=[]
for item in Inter_list:
    for link in item.find_all('a',class_='view_detail_button',href=True):
        Intern_link.append(baseurl+link['href'])
        # print(link['href'])

# print(Intern_link)
I_l=[]
l=''
testlink='https://internshala.com/internship/details/covid-emergency-langar-sewa-delivery-assistance-part-time-job-internship-at-noida-in-proof-of-performance-data-services-private-limited1620118753'
# for link in Intern_link:
#     if l!=link:
#         r=requests.get(link,headers=headers)
#         soup=BeautifulSoup(r.content,'lxml')
#         Intern_name=soup.find('div',class_='heading_4_5 profile').text.strip()
#         Comp_name=soup.find('a',class_='link_display_like_text').text.strip()
#         Location=soup.find('a',class_='location_link').text.strip()
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
#             'Stpend': Stpend
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
r=requests.get(testlink,headers=headers)
soup=BeautifulSoup(r.content,'lxml')
# opening=soup.find_next('div',attrs={'class':'section_heading heading_5_5'}).text
Comp_link=soup.find('div',class_='text-container.website_link',href=True)
print(Comp_link)