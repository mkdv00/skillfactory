# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body):
    page = f"<html>{head}{body}</html>"
    return page


def generate_head(title):
    head = f"""
    <head>
        <meta charset="Windows-1251">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{title}</title>
    </head>"""
    return head


def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1><hr>"
    copyright_year = dt.now().year
    copyright = "<p>" + "Copyright " + str(copyright_year) + "</p>"
    created_by = "<p>Создал - Maksim Kudaev</p>"
    for p in paragraphs:
        body += f"<p>{p}</p>"
    return f"""<body>{body}<hr><a href="about.html">О реализации</a><hr>{copyright}{created_by}</body>"""


def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w")
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs)
    )
    print(page, file=fp)
    fp.close()


today = dt.now().date()
# Generated index.html
save_page(
    title="Гороскоп на сегодня",
    header="Ваши предсказания на " + str(today),
    paragraphs=generate_prophecies()
)

# Generated about.html
save_page(
    title="О чём всё это",
    header=""
)
