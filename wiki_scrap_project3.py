import requests
from bs4 import BeautifulSoup

# 1. Ссылка на статью, которую ты открыл
url = "https://en.wikipedia.org/wiki/Tajikistan"

# 2. Просим Python "сходить" на сайт и скачать его содержимое
# Мы добавляем 'headers', чтобы сайт думал, что зашел человек через браузер
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# 3. Превращаем текст страницы в понятный "суп" из тегов
soup = BeautifulSoup(response.text, 'html.parser')

# 4. САМЫЙ ВАЖНЫЙ МОМЕНТ:
# Мы говорим: "Найди тег h1, у которого id равен firstHeading"
# Помнишь, ты это нашел в инспекторе?
heading = soup.find('h1', id='firstHeading')

# 5. Выводим только текст заголовка, без лишнего кода
print("Заголовок статьи:", heading.text)