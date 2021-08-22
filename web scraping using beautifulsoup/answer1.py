import requests
url1='https://my-json-server.typicode.com/typicode/demo/comments'
url2='https://my-json-server.typicode.com/typicode/demo/posts'
ds=requests.get(url1)
data1=ds.json()
ids=[id['id'] for id in data1]
dt=requests.get(url2)
data2=dt.json()
for i in range(len(data2)):
    try:
        if data2[i]['id']==data1[i]['id']:
            data2[i]['body']=data1[i]['body']
    except:
        data2[i]['body']=' '
dt=dict()
dt['data']=data2
print(dt)


"""
Output:-- 

{'data': [{'id': 1, 'title': 'Post 1', 'body': 'some comment'}, 
{'id': 2, 'title': 'Post 2', 'body': 'some comment'}, 
{'id': 3, 'title': 'Post 3', 'body': ' '}]}
"""
