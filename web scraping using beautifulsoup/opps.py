import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract(page):
    url=f'https://internshala.com/internships/page-{page}'
    headers={
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup

def transfrom(soup):
    I_l=[]
    divs=soup.find_all('div',class_='container-fluid individual_internship')
    for item in divs:
        title=item.find('a').text.strip()
        company=item.find('div',class_='heading_6 company_name').text.strip()
        Intern_link=('https://internshala.com'+str(item.find('a',class_='link_display_like_text',href=True)['href']))
        Location=item.find('a',class_='location_link').text.strip()
        Location_link=('https://internshala.com'+str(item.find('a',class_='location_link',href=True)['href']))
        try:
            Start_Date=item.find('span','start_immediately_desktop').text.strip()
        except:
            Start_Date="Immediately"
        Stipend=item.find('span','stipend').text.strip()
        Internship_Type=item.find('div',class_='label_container label_container_desktop').text.strip()
        
        
        
        
            
        Internship={
                    'Intern_name':title,
                    'Intern_link':Intern_link,
                    'Company_name': company,
                    'Location': Location,
                    'Location_link':Location_link,
                    'Start date': Start_Date,
                    'Stpend': Stipend

                    }
        I_l.append(Internship)
        # print('saving:',Location)
        # df=pd.DataFrame(I_l)
        
        # data=df.to_csv('intern.csv')


c=extract(1)
transfrom(c)




