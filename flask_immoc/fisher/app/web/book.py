from flask import jsonify,request
from app.lib.helper import is_isbn_or_key
from app.lib.httper import HTTP
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.web.blueprint_init import web

#路径参数
# @web.route("/book/search/<q>/<page>")
# def search(q,page):
#     isbn_or_key = is_isbn_or_key(q)
#     if isbn_or_key == 'isbn':
#         result = YuShuBook.search_by_isbn(q)
#     if isbn_or_key == 'key':
#         result = YuShuBook.search_by_keyword(q)
#     return jsonify(result)


@web.route("/book/search")
def search():
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        #从form中取数的好处，page空
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        if isbn_or_key == 'key':
            result = YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
    else:
        return jsonify(form.errors)