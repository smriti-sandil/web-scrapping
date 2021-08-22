import requests
from bs4 import BeautifulSoup
import pandas as pd
column = ['ID','Email','First_name','Last_name','Avatar']
dt=[]
for n in range(1,13):   
    URL = 'https://reqres.in/api/users?page='+str(n) 
    r=requests.get(URL)
    all_data=r.json()
    data1=all_data['data']
    print('page num--',n,' Number of users----> ',len(data1))
    for i in data1:
        data_list = [i['id'],i['email'],i['first_name'],i['last_name'],i['avatar']]
        dt.append(data_list)
df = pd.DataFrame(dt,columns=column)
df.to_csv('user_data.csv', index=False)











