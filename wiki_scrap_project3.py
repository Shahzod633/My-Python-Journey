import requests                                         # мы импортируем библитеку который даёт запрос на сайт 
from bs4 import BeautifulSoup                           # Этот раздел я не понял!!! 
url= "https://en.wikipedia.org/wiki/Tajikistan"         # здесь я указал ссылку который в долнешем будт проверять или анализировать 
headers = {'User-Agent': 'Mozilla/5.0'}                 # А здесь я использую загаловок это как Python не сам ишеет а через браузер mozillsa 5.0
response=requests.get(url, headers=headers)             # А это ответ от сайта отклик 
print(f'статус ответа {response.status_code}')          # здесь после придедушей команды он провкряет статус ответа от сайта или ответ отрецателтьный или положительный
soup=BeautifulSoup(response.text,'html.parser')         # после положительного ответа эмм тоже не понял!!!
sections=soup.find_all('h2')                            # А здесь команда sections ишет все раздели кода HTML в котором есть код h2 и вводит из всех потомучто я написал команду find.all
print(f'Найдено разделов: {len(sections)}')             # Выводит все найденнные разделы и их количество 
print("-" * 20)                                         # не понял
for section in sections:                                # А это цыкл который связанно со строкой 7 sections - он делает цыкличный запрос на сайт или ишеет все найденный h2 
    title=section.text.strip()                          #не понял
    print(f'Раздел: {title}')                           # не понял