# NGMT-News Digest 

Краткое Описание:
Next Gen Med Tech News Digest это веб приложение позволяющее читателям получать релевантные новости в сфере biomedical innovations. 
Сайт использует фильтрацию по категориям; genetics, medical AI, neuroscience, and biotech, а так же по типам контента; breakthroughs, opportunities, и explainers, 
предоставляя информацию из API в реальном времени.

Инструкция по установке и запуску:

1. Клонируйте репозиторий;
	"
	git clone https://github.com/ilshatrozy/ngmt-news.git
	cd ngmt-news
	"

2. Создайте virtual env:
	"
	python -m venv venv
	source venv/bin/activate #для MacOS/Linux
	venv/Scripts/activate #для Windows 
	"

3. Установите Requirements:
	"
	pip install -r requirements.txt
	"

4. Создайте .env файл и добавьте ваш API key:
	"
	API_KEY="ваш ключ"
	"

5. Запустите приложение и terminal выдаст вам ссылку с сайтом:
	"
	uvicorn ngmt:app --reload
	"

Описание процесса проектирования:
Для меня было важно поддерживать минимализм в дизайне и интерактивность чтобы сайт был простым но при этом не скучным. 
Так же мы не забыли про inclusivity, а именно цвета были подобраны так что люди с colour-blindness могли различать кнопки проще и им было удобнее.
Помимо этого, мы не забыли про модульность да бы читателям и интересующимся было легче анализировать код (fronted и backend logics разделены).

Основные этапы разработки:
1. Проектирование структуры FastAPI-приложения;
2. Интеграция шаблонов jinja2 и базы html/css UI;
3. Подключение внешнего Api (NewsAPI.org) для получения статей;
4. Реализация интерактивных элементов (анимация карточек и scroll-to-top);
5. Рефакторинг и опитимизация пользовательского опыта.






