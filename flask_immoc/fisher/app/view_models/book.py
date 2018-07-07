class _BookViewModel:
    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned
    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned
    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author':'、'.join(data['author']),
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book
#模板渲染的话应该在这处理，如果使用js操作，前台方便
#给前端列表，前端处理更为灵活
#如果有null 需要转化成空   否则渲染报错


class   BookViewModel:
    def __init__(self,book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = book['author']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''
    def fill(self,yushu_book,keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book)  for book in yushu_book.books]