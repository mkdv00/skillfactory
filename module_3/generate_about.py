# coding: utf-8

from horoscope import *
from datetime import datetime as dt

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


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


def generate_body(header, times, advices, promises):
    body = f"<h1>{header}</h1><hr>"
    copyright_year = dt.now().year
    copyright = "<p>" + "Copyright " + str(copyright_year) + "</p>"
    created_by = "<p>Создал - Maksim Kudaev</p>"
    body += """<img src="https://www.1ori.ru/images/horoscope.gif">
    <p>Гороскоп был создан при помощи рандомного подбора следующих слов:</p>
    <h2>1 Времена дня:</h2>"""
    for time in times:
        body += f"""<ul>
                        <li>{time}</li>
                    </ul>"""
    body += "<h2>2 Глаголы:</h2>"
    for advice in advices:
        body += f"""<ul>
                        <li>{advice}</li>
                    </ul>"""
    body += "<h2>3 Действия:</h2>"
    for promise in promises:
        body += f"""<ul>
                        <li>{promise}</li>
                    </ul>"""
    return f"""<body>{body}<hr><a href="index.html">На главную</a><hr>{copyright}{created_by}</body>"""


def save_page(title, header, times, advices, promises, output="about.html"):
    fp = open(output, "w")
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, times=times, advices=advices, promises=promises)
    )
    print(page, file=fp)
    fp.close()


today = dt.now().date()
# Generated about.html
save_page(
    title="О чём всё это",
    header="О чём всё это",
    times=times,
    advices=advices,
    promises=promises
)
