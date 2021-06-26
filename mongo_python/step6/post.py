
from databse import Database
import uuid
import datetime
# unserstadning Dates in python- datetime modules

class Post:
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow() , id=None ):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id
        
        #How to use this class
        #post = Post(blog_id="123", title="a title", content="some content", author="Jose", date=datetime.datetime.utcnow())
        
    def save_to_mongodb(self):
        Database.insert( collection='posts',  data=self.json() )
        
    def json(self):
        return {
            'id': self.id,
            'title' : self.title,
            'blog_id' : self.blog_id,
            'content' : self.content,
            'author' : self.author,
            'created_date' : self.date
            
            }
    @staticmethod
    def from_mongo(id):
        return Database.find_one( collection='posts', query={'id': id })
    
    @staticmethod
    def from_blog(id):
        return [ post for post in Database.find( collection='posts', query={'blog_id': id })]