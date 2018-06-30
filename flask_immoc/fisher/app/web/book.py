from flask import jsonify
from helper import is_isbn_or_key
from httper import HTTP
from yushu_book import YuShuBook

from app.web import web


@web.route("/book/search/<q>/<page>")
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    if isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
