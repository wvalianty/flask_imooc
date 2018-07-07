from flask import jsonify,request
from app.lib.helper import is_isbn_or_key
from app.lib.httper import HTTP
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.web.blueprint_init import web
from app.view_models.book import BookViewModel,BookCollection
import json
#路径参数
# @web.route("/book/search/<q>/<page>")
# def search(q,page):
#     isbn_or_key = is_isbn_or_key(q)
#     if isbn_or_key == 'isbn':
#         result = YuShuBook.search_by_isbn(q)
#     if isbn_or_key == 'key':
#         result = YuShuBook.search_by_keyword(q)
#     return jsonify(result)

#接口好用不好用考量   返回数据全面   返回数据好用  搜索  关键字  条数
@web.route("/book/search")
def search():
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        #从form中取数的好处，page空
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        if isbn_or_key == 'key':
            yushu_book.search_by_keyword(q,page)
        books.fill(yushu_book,q)
        return json.dumps(books,default=lambda o:o.__dict__),{'content-type':'application/json'}
    else:
        return jsonify(form.errors)