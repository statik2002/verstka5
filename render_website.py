import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from livereload import Server, shell

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    with open('books/books.json', 'r') as books_file:
        books_json = books_file.read()

    books = json.loads(books_json)

    chunked_books = list(chunked(books, 2))

    rendered_page = template.render(
        books=chunked_books
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


on_reload()
server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
