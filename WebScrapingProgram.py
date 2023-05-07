import requests

from bs4 import BeautifulSoup as bs
print('Get ready to execute your first python program ')
github_user= input('input Github user: ')
url= 'https://github.com/'+ github_user
r= requests.get(url)
soup= bs(r.content, 'html.parser')
profile_image= soup.find('img', {'width' :'260'})['src']
print(profile_image)
print('Click on the above link to see your profile\nThanks')