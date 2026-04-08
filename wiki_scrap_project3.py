# мы импортируем библитеку который даёт запрос на сайт 
# Расширение BeautifulSoup!!! 
import requests 
from bs4 import BeautifulSoup
# здесь я указал ссылку который в долнешем будт проверять или анализировать                            
url="https://somon.tj/nedvizhimost/prodazha-kvartir/hudzhand/"
 # А здесь я использую загаловок это как Python не сам ишеет а через браузер mozillsa 5.0 
headers = {'User-Agent': 'Mozilla/5.0'}     
 # здесь после придедушей команды он провкряет статус ответа от сайта или ответ отрецателтьный или положительный           
response=requests.get(url, headers=headers)             
print(f'статус ответа {response.status_code}')          
soup=BeautifulSoup(response.text,'html.parser')       
cards=soup.find_all('div', class_='advert')  
print(f'Найдено разделов: {len(cards)}')             
print("-" * 40)                                        
for card in cards:
    # Ищем элементы
    title_el = card.find('a', class_='advert__content-title')
    price_el = card.find('div', class_='advert__content-header')
    
    # ПРОВЕРКА (как на Stepik): если оба элемента существуют
    if title_el and price_el:
        # .replace('\n', ' ') убирает прыжки на новую строку внутри текста
        title = title_el.text.strip().replace('\n', ' ')
        price = price_el.text.strip().replace('\n', ' ')
        link = "https://somon.tj" + title_el.get('href')

        # Выводим всё в одну строку или компактным блоком без лишних пустых print
        print(f"🏠 {title}")
        print(f"💰 Цена: {price}")
        print(f"🔗 {link}")
        print("-" * 10) # Короткая линия, чтобы не растягивать экран