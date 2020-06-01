# coding: utf-8
import os
from bottle import request, route, run
from my_logging import get_logger

logger = get_logger("divider-server")

@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    res = {"result": 0, "error": None}
    try:
        res["result"] = top / bottom
    except Exception as err:
        res["error"] = f"Для входных данных {top} и {bottom} не получилось:{err}"
        agent = request.headers["User-Agent"]
        host = request.headers["Host"]
        path = request.path
        logger.error(f"Ошибка деления при обращении к {host}{path}. User-Agent:{agent}")

    return res


if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
