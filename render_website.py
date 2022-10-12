import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from itertools import count
from pathlib import Path
from pprint import pprint

from livereload import Server, shell

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked, ichunked


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    with open('books/books.json', 'r') as books_file:
        books_json = books_file.read()

    books = json.loads(books_json)

    pages_dir = 'pages'

    Path(pages_dir).mkdir(exist_ok=True)

    all_chunks = ichunked(books, 10)

    page_count = 1
    for chunked_page in all_chunks:

        chunked_books = list(chunked(chunked_page, 2))

        rendered_page = template.render(
            chunked_books=list(chunked_books)
        )

        with open(Path(pages_dir).joinpath(f'index{page_count}.html'), 'w', encoding="utf8") as file:
            file.write(rendered_page)

        page_count += 1


on_reload()
server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
