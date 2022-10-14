# Скрипт для создания статических страниц библиотеки

## Общее описание

Скрипт создает набор статических страниц html с книгами в директории `pages`. Данные берет 
из директории `books`, в которой лежат тексты книг, изображения обложек и файл `books.json`.

![Скриншот сайта библиотеки](screen.png)

## Установка

Создать виртуальное окружение командой:
```
python3 -m venv env
```

Войти в виртуальное окружение командой:
```
source env/bin/activate
```

Установить зависимости командой:
```
pip install -r requirements.txt
```

## Использование

Запустить скрипт командой:
```
python render_website.py
```

В результате в директории `pages` будут сформированы страницы сайта. Теперь можно 
открывать любой файл со страницами книг в этой директории и просматривать книги в вашем браузере по 
этой ссылке [http://127.0.0.1:5500/](http://127.0.0.1:5500/).

Демонстрация библиотеки находиться [по этой ссылке](https://statik2002.github.io/verstka5/pages/index1.html).